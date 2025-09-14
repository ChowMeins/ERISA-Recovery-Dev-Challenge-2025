from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
import random
from django.shortcuts import redirect, render
from .models import ERISA_User

# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        if not username or not password:
            messages.error(request, "Please fill in both username and password.")
            return render(request, "login.html")

        # authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)  # log the user in
                return redirect('/claims/')  # or any page you want
            else:
                messages.error(request, "This account has been deactivated.")
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, "login.html")

def sign_up(request):
    if request.method == "POST":
        # extract form data
        username = request.POST['username']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']

        if not username or not password:
            messages.error(request, "Please fill in all required fields")
            return render(request, "sign_up.html")
        # generate a unique 6-digit id
        user_id = random.randint(100000, 999999)

        # create the user
        user = ERISA_User.objects.create_user(
            id=user_id,
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name
        )

        return redirect('/login/')  # wherever you want post-signup
    else:
        # GET request → just render the sign-up form
        return render(request, "sign_up.html")