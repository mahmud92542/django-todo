from django import forms
from .models import *


class WorkForm(forms.ModelForm):
    class Meta:
        model = Work
        fields = ('title',
                  'description',
                  'status',
                  'remarks',
                  'createdby'
                  )
