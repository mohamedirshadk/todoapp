from django.urls import path
from todoapp.views import TodoAppHomeView,TodoListView,TodoCreateView,TodoUpdateView,TodoDeleteView,TodoDetailView



urlpatterns = [
    path('',TodoAppHomeView.as_view(),name='todoapp'),
    path('create/',TodoCreateView.as_view(),name='todo_create'),
    path('list/',TodoListView.as_view(),name='todo_list'),
    path('detail/<int:pk>/',TodoDetailView.as_view(),name='todo_detail'),
    path('update/<int:pk>/',TodoUpdateView.as_view(),name='todo_update'),
    path('delete/<int:pk>/',TodoDeleteView.as_view(),name='todo_delete'),
]