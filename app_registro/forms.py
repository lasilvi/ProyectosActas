from django import forms
from .models import Act,User,Development,Responsibledevelopment,Commitment
from django.forms import formset_factory

class RegisterForm(forms.ModelForm):
    class Meta:
        """Campos utilizados."""
        model = Act
        fields = "__all__"
        widgets = {
            'pub_date': forms.DateTimeInput(attrs={'class': 'form-control datetimepicker'})
        }
      

class RegisterFormUser(forms.ModelForm):
    class Meta:
        """Campos utilizados."""
        model = User
        fields = "__all__"
    

class RegisterFormDevelopment(forms.ModelForm):
    #nombre = forms.CharField(min_length=3)
    class Meta:
        """Campos utilizados."""
        model = Development
        fields = "__all__"

class RegisterFormDevelopment(forms.ModelForm):
    #nombre = forms.CharField(min_length=3)
    class Meta:
        """Campos utilizados."""
        model = Development
        fields = "__all__"

class RegisterFormResponsibledevelopment(forms.ModelForm):
    #nombre = forms.CharField(min_length=3)
    class Meta:
        """Campos utilizados."""
        model = Responsibledevelopment
        fields = "__all__"
        
DevelopmentFormSet = formset_factory(RegisterFormDevelopment, extra=1)
ResponsibleDevelopmentFormSet = formset_factory(RegisterFormResponsibledevelopment, extra=1)

class RegisterFormCommitment(forms.ModelForm):
    #nombre = forms.CharField(min_length=3)
    class Meta:
        """Campos utilizados."""
        model = Commitment
        fields = "__all__"