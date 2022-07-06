from django import forms
from .models import Setor

class SetorEditForm(forms.ModelForm):
    class Meta:
        model = Setor

        fields = ['descricao']