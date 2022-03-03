from django.forms import ModelForm
from todoapp.models import TodoItemModel


class TodoItemForm(ModelForm):
    class Meta:
        model = TodoItemModel
        fields = ['title']
