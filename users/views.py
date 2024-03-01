from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from users.form import UserForm
from users.models import UserModel


# Create your views here.

class CreateUserView(CreateView):
    model = UserModel
    form_class = UserForm
    template_name = 'create_update_form.html'
    success_url = reverse_lazy('users=all')


class UserListView(ListView):
    model = UserModel
    template_name = 'users/all.html'

class UserUpdateView(UpdateView):
    model = UserModel
    form_class = UserForm
    template_name = 'create_update_form.html'
    success_url = reverse_lazy('users-all')

class UserDeleteView(DeleteView):
    model = UserModel
    template_name = 'delete_form.html'
    success_url = reverse_lazy('users-all')

class UserDetailView(DetailView):
    model = UserModel
    template_name = 'users/detalii.html'


