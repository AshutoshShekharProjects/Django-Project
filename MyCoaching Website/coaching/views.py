from django.shortcuts import render,redirect
#from django.http import HttpResponse
#from django.contrib import messages
#from django.contrib.auth.models import User,auth
from . models import Coachings,Query


def index(request):
    coaching = Coachings.objects.all()
    return render(request, 'index.html', {'coaching':coaching})


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method=='POST':
        your_name=request.POST['your_name']
        your_email=request.POST['your_email']
        subject=request.POST['subject']
        message=request.POST['message']
        msg=Query(your_name=your_name,your_email=your_email,subject=subject,message=message)
        #msg=Query.objects.raw('''Insert INTO Query
                              #(your_name,your_email,subject,message)
                              #VALUES(?,?,?,?)''',(your_name,your_email,subject,message))
        msg.save()
        return render(request, 'contact.html')
    else:
        return render(request,'contact.html')


'''def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            messages.info(request,'Invalid Username or Password')
            return redirect('login')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"User Exists")
                return redirect('redirect1')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email Exists")
                return redirect('redirect1')
            else:
                user=User.objects.create(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                messages.info(request,'Successful')
                return redirect('login')
        else:
            messages.info(request,'Password did not match')
            return redirect('register')
        return redirect('register')
    else:
        return render(request,'register.html')'''
