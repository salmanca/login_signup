from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def sign_up(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username_in = request.POST['username']
            if not username_in == '' :
                if not User.objects.filter(username = username_in):
                    email = request.POST['email']
                    firstname_in = request.POST['first_name']
                    lastname_in = request.POST['last_name']
                    if request.POST['password1'] == request.POST['password2'] and not request.POST['password1']  == '':
                        password_in = request.POST['password1']
                        user_entery = User.objects.create_user(username_in, email, password_in)
                        user_entery.first_name = firstname_in
                        user_entery.last_name = lastname_in
                        user_entery.save()
                        checked = request.POST.get('checked')
                        if checked: 
                            user = authenticate(ussername = username_in, password = password_in)
                            if user is not None:
                                login(request, user)
                                return redirect(request, 'home_page')
                            else:
                                messages.success(request, ("Registered successfully"))
                                return redirect('login_user')
                        else:
                            messages.success(request, ("Registered successfully"))
                            return redirect('login_user')
                    else:
                        messages.success(request, ("Password does not match"))
                        return render(request, 'signup.html')
                else:
                    messages.success(request, ("Username already exist"))
                    return redirect('sign_up')
            else:
                messages.success(request, ("Username must be provided"))
                return render(request, 'signup.html')
            
        else:
            return render(request, 'signup.html')  
    else:
        return render(request, 'home.html')
    
def login_user(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username_in = request.POST['username']
            password_in = request.POST['password']
            user = authenticate(username = username_in, password = password_in)
            if user is not None:
                login(request,user)
                return render(request, 'home.html')
            else:
                messages.success(request, ("Invalid Username or Password"))
                return redirect('login_user')
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'home.html')

def home_page(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        return redirect('login_user')

def logout_user(request):
    logout(request)
    messages.success(request, ("Loged out successfuly"))
    return redirect('login_user')