from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.decorators import login_required
from .forms import LoginForm

# Create your views here.
#Custom created view
# def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request,username=username,password=password)
#             if user is None:
#                 return HttpResponse('Invalid login')
#             login(request,user)
#             return HttpResponse('Authenticated successfully')
#     else:
#         form = LoginForm()
#     return render(request,'accounts/login.html',{"form":form})

@login_required
def dashboard(request):
    return render(request,"accounts/dashboard.html") 