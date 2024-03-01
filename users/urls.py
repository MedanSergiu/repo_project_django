"""
URL configuration for new_business project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from users.views import *


from home.views import HomeView

urlpatterns = [
    path('', UserListView.as_view(), name='users-all'),
    path('add/', CreateUserView.as_view(), name='users-add'),
    path('detalii/<int:pk>', UserDetailView.as_view(), name='users-detail'),
    path('update/<int:pk>', UserUpdateView.as_view(), name='users-edit'),
    path('delete/<int:pk>', UserDeleteView.as_view(), name='users-delete'),

]
