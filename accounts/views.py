from django.contrib import messages
from django.contrib.auth import tokens
from accounts.models import Account
# from django.forms import Form
from django.shortcuts import redirect, render
from .forms import RegistrationForms
from .models import Account
from django.contrib import messages,auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

#verification email
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from bus.models import Seat

# Create your views here.
#views for accounts

def register(request):
    if request.method=='POST':
        form= RegistrationForms(request.POST)
        if form.is_valid():
            first_name= form.cleaned_data['first_name']
            last_name= form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email= form.cleaned_data['email']
            password = form.cleaned_data['password']
            username= email.split("@")[0]
            user = Account.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
            user.phone_number = phone_number
            user.save()
            #user activation-----------
            current_site =get_current_site(request)
            mail_subject = 'Please activate your account'
            message = render_to_string('accounts/account_verification_email.html', {
                'user':user,
                'domain':current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email=email
            send_email= EmailMessage(mail_subject, message, to=[to_email])
            print(to_email)
            send_email.send()

            messages.success(request, 'Registration Successful!')
            return redirect('/accounts/login/?command=verification&email='+email)

    else:
        form = RegistrationForms()
    context={
        'forms':form
    }
    return render(request, 'accounts/register.html',context)

def login(request):
    if request.method =='POST':
        email   =request.POST['email']
        password=request.POST['password']
        
        user= auth.authenticate(email=email, password=password)      

        if user is not None:
            auth.login(request, user)
            messages.success(request,'You are now Logged In!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid Login Credentials')
            return redirect('login')
    return render(request, 'accounts/login.html')
    
@login_required(login_url = 'login')
def logout(request):
    auth.logout(request)
    messages.success(request, 'You are logged out.')
    return redirect('login')


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user,token):
        user.is_active =True
        user.save()
        messages.success(request, 'congratulation! Your account is activated.')
        return redirect('login')
    else:
        messages.error(request, 'Invalid activation link')
        return redirect('register')




def forgotpassword(request):
    if request.method =='POST':
        email= request.POST['email']
        if Account.objects.filter(email=email).exists():
            user = Account.objects.get(email__exact=email)  
            #reset password verification
            current_site =get_current_site(request)
            print(current_site)
            mail_subject = 'Please reset your password'
            message = render_to_string('accounts/reset_password_email.html', {
                'user':user,
                'domain':current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email=email
            send_email= EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()

            messages.success(request,'password reset email has been sent your email address')
            return redirect('login')
        else:
            messages.error(request,'Account doesnot exist!')
            return redirect('forgotpassword')
    return render(request, 'accounts/forgotpassword.html')

def resetpassword_validate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except(TypeError, ValueError,OverflowError, Account.DoesNotExist):
        user = None
    
    if user is not None and default_token_generator.check_token(user,token):
        request.session['uid'] = uid
        messages.success(request, 'please reset your password')
        return redirect('resetpassword')
    else:
        messages.error(request,"This link has been expired")
        return redirect('login')

def resetpassword(request):
    if request.method =='POST':
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            uid = request.session.get('uid')
            user = Account.objects.get(pk=uid)
            user.set_password(password)
            user.save()
            messages.success(request,'password reset successful, Login')
            return redirect('login')
        else:
            messages.error(request, 'Password doesnot match!')
            return redirect('restpassword')
    else:
        return render(request, 'accounts/resetpassword.html')

