
from django.urls import path
from general.views import AboutView, ContactView, HomeView,UserCreateView,  UserListView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('contactus/', ContactView.as_view(), name='contactus'),
    path('user/create/', UserCreateView.as_view(), name='user_create'),
    path('user/list/', UserListView.as_view(), name='user_list'),

]
