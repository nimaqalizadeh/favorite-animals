# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required


# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('animal:list')
#     return render(request, 'accounts/login.html')

# @login_required
# def logout_view(request):
#     if request.user.is_authenticated:
#         logout(request)
#     return redirect('accounts:login')

# from django.shortcuts import render, redirect
# from django.contrib.auth import login, authenticate, logout
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib import messages

# # Registration view
# def register_view(request):
#     if request.method == "GET":
#         form = UserCreationForm()
#         return render(request, "accounts/register.html", {"form": form})


#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             messages.success(request, "Registration successful.")
#             return redirect("animals:list_animal")  # Redirect to home page after successful registration
#         else:
#             messages.error(request, "Registration failed. Please correct the errors below.")
#     return render(request, "accounts/register.html", {"form": form})

# # Login view
# def login_view(request):

#     if request.method == "GET":
#         form = AuthenticationForm()
#         return render(request, "accounts/login.html", {"form": form})

#     if request.method == "POST":
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get("username")
#             password = form.cleaned_data.get("password")
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 messages.success(request, f"Welcome back, {username}!")
#                 return redirect("animals:list_animal")  # Redirect to home page after successful login
#             else:
#                 messages.error(request, "Invalid username or password.")
#                 form = AuthenticationForm()
#                 return render(request, "accounts/login.html", {"form": form})
#         else:
#             messages.error(request, "Invalid username or password.")
#     return render(request, "accounts/register.html", {"form": form})


# # Logout view
# def logout_view(request):
#     logout(request)
#     messages.info(request, "You have successfully logged out.")
#     return redirect("login")


from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages

# Registration view
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("animals:list_animals")
        else:
            messages.error(request, "Registration failed. Please correct the errors below.")
    else:
        form = UserCreationForm()
    return render(request, "accounts/register.html", {"form": form})

# Login view
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {user.username}!")
                return redirect("animals:list_animals")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})

# Logout view
def logout_view(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("accounts:login")
