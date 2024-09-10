from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

#Modify your forms here
class CustomUserCreationForm(UserCreationForm): #Creación del usuario con nombre, email y edad
    class Meta(UserCreationForm):
        model = CustomUser
        fields = (
            'username',
            'email',
            'age',
        )
        
class CustomUserChangeForm(UserChangeForm): #Cambio del usuario con nombre, email y edad
    class Meta:
        model = CustomUser
        fields = (
            'username',
            'email',
            'age',
        )