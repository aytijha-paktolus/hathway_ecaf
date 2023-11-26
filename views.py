from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from .models import CustomUser
from fernet import Fernet

def register_user(request):

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the user registration data

            # Handle image upload
            if 'image' in request.FILES:
                image = request.FILES['image']

                # Encrypt the image
                key = Fernet.generate_key()
                f = Fernet(key)
                encrypted_image = f.encrypt(image.read())

                # Save the encrypted image
                with open(f'images/{image.name}', 'wb') as f:
                    f.write(encrypted_image)

                # Store encrypted image path in database
                image_path = f'images/{image.name}'
                user = CustomUser.objects.get(username=form.cleaned_data['username'])
                user.image_path = image_path
                user.save()

            return redirect('login')

    else:
        form = UserRegistrationForm()

    return render(request, 'registration/register.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm

def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the user registration data

            # Handle image upload
            if 'image' in request.FILES:
                image = request.FILES['image']

                # Encrypt the image
                key = Fernet.generate_key()
                f = Fernet(key)
                encrypted_image = f.encrypt(image.read())

                # Save the encrypted image
                with open(f'images/{image.name}', 'wb') as f:
                    f.write(encrypted_image)

                # Store encrypted image path in database
                image_path = f'images/{image.name}'
                user = CustomUser.objects.get(username=form.cleaned_data['username'])
                user.image_path = image_path
                user.save()

            return redirect('login')

    else:
        form = UserRegistrationForm()

    return render(request, 'registration/register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('login')

@login_required
def home_page(request):
    return render(request, 'home.html')