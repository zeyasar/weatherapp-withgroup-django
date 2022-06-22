from django.contrib import admin
from django.urls import path

from users.views import user_login, register, user_logout


urlpatterns = [
    path('login/', user_login, name='user_login'),
    path('register/', register, name='register'),
    path('logout/', user_logout, name='user_logout'),

]