from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm, LoginForm
from django.contrib import messages
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request,'index.html', {'posts':posts})

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def user_signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request, "Congratulations!! You have become an Author.")
            form.save()
    else:
        form = SignUpForm()
    return render(request,'signup.html',{'form':form})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.changed_data['username']
                upass = form.changed_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in Successfully !!')
                    return HttpResponseRedirect('/dashboard')
        else:
            form = LoginForm()
        return render(request, 'login.html', {'form':form})
    else:
        return HttpResponseRedirect('/dashboard/')