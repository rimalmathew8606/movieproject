
from django import forms

from movieshows.models import movieshows


class movieform(forms.ModelForm):
    class Meta:
        model = movieshows
        fields = "__all__"
