# from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView
from general.forms import UserForm
from general.models import UserModel


# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'


class AboutView(TemplateView):
    template_name = 'about.html'


class ContactView(TemplateView):
    template_name = 'contactus.html'


class UserCreateView(CreateView):
    template_name = 'user_create.html'
    form_class = UserForm
    success_url = "/user/create/"


class UserListView(ListView):
    model = UserModel
    template_name = 'user_list.html'
