from django.forms import ModelForm as md
from accounts.models import *


class MovieForm(md):
    class Meta:
        model = Movie
        fields = "__all__"
