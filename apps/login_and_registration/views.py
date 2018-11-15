from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
import bcrypt

def index(request):
    return render(request, 'login_and_registration/index.html')

def register_account(request):
    if request.method == "POST":
        errors = User.objects.basic_validation(request.POST)
        if len(errors) > 0:
            for k, v in errors.items():
                messages.error(request, v)
            return redirect('/')
        else:
            p_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
            print(p_hash)
            User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], p_hash = p_hash)
            return redirect('/success')

def show_success(request):
    
    return render(request, 'login_and_registration/success.html')

def validate_and_login(request):
    if request.method == "POST":
            errors = User.objects.login_validation(request.POST)
            if len(errors) > 0:  
                    for k, v in errors.items():
                        messages.error(request, v)
                    return redirect('/')
            else:
                    return redirect('/success')