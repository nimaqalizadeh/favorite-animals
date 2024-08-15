FROM  python:3.10.14-alpine3.20

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUBUFFERED 1

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD while ! python3 ./manage.py sqlflush > /dev/null 2&1; do sleep 1; done &&\ 
    python3 ./manage.py makemigrations --noinput && \
    python3 ./manage.py migrate --noinput && \
    python3 ./manage.py runserver 0.0.0.0:8000 