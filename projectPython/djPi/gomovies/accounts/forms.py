from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from accounts.models import Customer, Movie, Serverlink


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CustomerProfile(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']


class OneMovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'


class ServerUpdate(ModelForm):
    class Meta:
        model = Serverlink
        fields = '__all__'
        exclude = ['name']
