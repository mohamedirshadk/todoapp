from django.forms import ModelForm
from general.models import UserModel



class UserForm(ModelForm):
    class Meta:
        model = UserModel
        exclude = ('status','created_on','updated_on')