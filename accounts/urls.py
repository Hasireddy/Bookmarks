from django.urls import path
import django.contrib.auth.views as auth_views
from . import views

urlpatterns = [
    # path('login/',views.user_login,name="login")
    path('',views.home_view,name="home"),
    path('login/',auth_views.LoginView.as_view(),name='login'),
    path('logged_out/',auth_views.LogoutView.as_view(),name='logged_out'),
    path('dashboard/',views.dashboard,name="dashboard"),
    #password urls
    path('password-change/',auth_views.PasswordChangeView.as_view(),name="password_change"),
    path("password-change/done/",auth_views.PasswordChangeDoneView.as_view(),name="password_change_done"),
    #Password-reset view is to send email
    path('password-reset/',auth_views.PasswordResetView.as_view(),name="password_reset"),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(),name="password_reset_done"),
    #This view will work once user clicks on the link sent to the email
    path('password-reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    path('password-reset/complete',auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete")
    
]



#Templates for password reset rendered
#1.password_reset.html - redirects to the password reset form page where it asks for email to send the verification link
#2. password_reset_email.html - Contains the content of the link to be sent
#3. password_reset_done.html- Displays message to the user that a verification link has been sent
#4. password_reset_confirm.html -  Contains the form to reset the Password if its a valid link
#5. password_reset_complete.html- displays a successful msg that password reset successfully