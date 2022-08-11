from django import forms
from .models import *


class NoticeForm(forms.ModelForm):

    class Meta:
        model = Notice
        fields = ["is_public", "title", "text"]


