from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
import bcrypt
from apps.login_and_registration.helpers.helpers import generate_word



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
            return redirect('/wall')

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
                    logged_in_user = User.objects.get(email = request.POST['email'])
                    request.session['logged_in_user_id'] = logged_in_user.id
                    random_word = generate_word()
                    request.session['random_word'] = random_word
                    # request.session['random_hash'] = bcrypt.hashpw(random_word.encode(), bcrypt.gensalt())
                    # random_hash = str(request.session['random_hash'], "utf-8")
                    # print(f"look, it worked this {random_hash} is a string")

                    return redirect("/wall?random_word={}".format(random_word))
