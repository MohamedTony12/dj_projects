from cmath import log
from django.shortcuts import render,redirect
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes,force_str
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .tokens import generate_token
from .forms import RegisterForm,LoginForm
from .models import AccountCustom


def send_mail_user(user,request):
    subject = 'account active'
    body = render_to_string('account/account_reset/email_active.html',{
        'user':user,
        'uid':urlsafe_base64_encode(force_bytes(user.id)),
        'domain':get_current_site(request).domain,
        'token':generate_token.make_token(user)
    })
    email_send = EmailMessage(
        subject=subject,
        body=body,
        from_email=settings.EMAIL_FROM_USER,
        to=[user]
    )
    email_send.send()

def account_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            n = form.save(commit=False)
            n.email = form.cleaned_data.get('email')
            n.set_password(form.cleaned_data.get('password1'))
            n.save()
            send_mail_user(n,request)
            messages.success(request,'please check your email to activate your account')
            return redirect('/')
    else:
        form = RegisterForm()        
    return render(request,'account/account_user/regsiter.html',{'form':form})

def account_activate(request,uidb64,token):
    uid = urlsafe_base64_decode(force_str(uidb64))
    try:
        user = AccountCustom.objects.get(id=uid)
    except:
        pass

    if user and generate_token.check_token(user,token):
        user.is_active = True
        user.save()
        messages.success(request,'Thanks for Visit us')
        return redirect('/')
    return render(request,'account/account_user/404.html')        


def account_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request,email=email,password=password)
            if user:
                login(request,user)
                messages.success(request,'Welcome Back')
                return redirect('/')
    else:
        form = LoginForm()
    return render(request,'account/account_user/login.html',{'form':form})  

@login_required
def account_logout(requset):
    user = requset.user
    if user.is_authenticated:
        messages.success(requset,'Thanks for Visit us')
        logout(requset)
        return redirect('/')