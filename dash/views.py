from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignupForm
from .models import Customer_db

# Create your views here.
def home(request):
    records = Customer_db.objects.all()


    if request.method == 'POST':
        username = request.POST['user_name']
        password = request.POST['password']

        user = authenticate(request, username = username, password=password)
        if user is not None: 
            login(request, user)
            messages.success(request, "You have logged in successfully!")
        else:
            messages.success(request, "You are not logged in, please try again.")
        return redirect('home')
    else:
        return render(request, 'home.html', {'records':records})

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out!")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username = username, password=password)
            login(request, user)
            messages.success(request, "Your account has been created successfully!")
            return redirect('home')
    else:
        form = SignupForm()
        return render(request, 'register.html', {'form':form})
    return render(request, 'register.html', {'form':form})