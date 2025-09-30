from django.urls import path
from users.views import register, user_login, user_defined_login
urlpatterns = [
    path('',user_login,name="user-login"),
    path('userlogin',user_defined_login, name="user-login"),
    path('register',register, name="user-register"),

]
