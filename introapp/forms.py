from django.forms import ModelForm
from .models import comentario
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CommentForm(ModelForm):
    class Meta:
        model = comentario
        fields = ('nombre','email','contenido','active')

class NewRegister(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username','password1','password2']
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Nombre de usuario'
        self.fields['password1'].label = 'Contraseña'
        self.fields['password2'].label = 'Confirmar contraseña'
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
        
    #create user
    def save(self, commit=True):
        user = super(NewRegister, self).save(commit=False)
        user.username = self.cleaned_data['username']
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user