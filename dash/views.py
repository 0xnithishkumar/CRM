from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignupForm, AddrecordForm
from .models import Customer_db
from datetime import datetime

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

def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record =  Customer_db.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record':customer_record})
    else:
        messages.success(request, "You must be logged in to view the page!")
        return redirect('home')
    
def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Customer_db.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Record deleted successfully!")
        return redirect('home')
    else:
        messages.success(request, "You must be logged in to delete the record!")
        return redirect('home')
    
def add_record(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AddrecordForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "The record has been added!")
                return redirect('home')
        else:
            form = AddrecordForm()
            return render(request, 'add_record.html', {'form':form})
    else:
        messages.success(request, "You must be logged in to add a record!")
        return redirect('home')
    
def update_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Customer_db.objects.get(id=pk)
        customer_record.updated_on = datetime.now()
        if request.method == 'POST':
            form = AddrecordForm(request.POST, instance=customer_record)
            if form.is_valid():
                form.save()
                messages.success(request, "The record has been updated!")
                return redirect(f'/record/{pk}')
        else:
            form = AddrecordForm(instance=customer_record)
            return render(request, 'update_record.html', {'form':form})
    else:
        messages.success(request, "You must be logged in to update a record!")
        return redirect('home')