from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login
from .forms import LoginForm

# Create your views here.

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user is None:
                return HttpResponse('Invalid login')
            login(request,user)
            return HttpResponse('Authenticated successfully')
    form = LoginForm()
    return render(request,'account/login.html',{"form":form})