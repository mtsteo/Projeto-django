from django import forms  
from .models import jogos, administradores


class jogoForm(forms.ModelForm):  
    class Meta:  
        model = jogos
        fields = "__all__"

class AdminForm(forms.ModelForm):
    class Meta: 
        model = administradores
        fields = "__all__"