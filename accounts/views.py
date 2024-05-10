from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm,UserCreationForm


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
                # if user.is_active:
#             login(request,user)
#             return HttpResponse('Authenticated successfully')
#     else:
#         form = LoginForm()
#     return render(request,'accounts/login.html',{"form":form})


#custom registerview


def user_register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('login')
            return HttpResponse("User created successfully")
        else:
            return render(request,"registration/register.html",{'form':form})
    form = UserCreationForm()
    return render(request,"registration/register.html",{'form':form})
    
    


# def user_register_view(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid:
#             # form.save()
#             # username = form.cleaned_data.get('username')
#             # raw_password = form.cleaned_data.get('password1')
#             return HttpResponse("User created successfully")
#         else:
#             return render(request,"registration/register.html",{'form':form})
#     form = UserCreationForm()
#     return render(request,"registration/register.html",{'form':form})
            
    

@login_required
def dashboard(request):
    return render(request,"accounts/dashboard.html") 

def home_view(request):
    return render(request,"registration/home.html")


@login_required
def user_profile(request):
    return render(request,"registration/user_profile.html",{})

@login_required
def user_profile_update(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('user_profile')
    else:
        form = UserChangeForm(instance=request.user)
        return render(request,'accounts/profile_update.html',{'form':form})
        
   
    