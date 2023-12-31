"""registration URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

from app.views import entry_list,create_entry
from app.views import entry_edit_view
from app.views import entry_delete_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.SignupPage,name='signup'),
    path('login',views.LoginPage,name='login'),
    path('home',views.home,name='home'),
    path('logout',views.LogoutPage,name='logout'),
    path('create_entry', create_entry, name='create_entry'),
    path('entry_list', entry_list, name='entry_list'),
    path('edit_entry/<int:pk>/', entry_edit_view, name='edit_entry'),
    path('delete_entry/<int:pk>/', entry_delete_view, name='delete_entry'),


]
