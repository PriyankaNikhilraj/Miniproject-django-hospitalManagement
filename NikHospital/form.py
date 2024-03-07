from django import forms
from .models import Login,Registration,Booking
class formz(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'container'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'container'}))
    class Meta:
        model = Login
        fields = ['email','password']

    # email = forms.CharField(max_length=50)
    # password = forms.CharField(widget=forms.PasswordInput)
class formz2(forms.ModelForm):
    name=forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class': 'form-control'}))
    phon=forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'container'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class': 'container'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'container'}))
    # confirm_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Registration
        fields = ['name','phon','email','password']



class formz3(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name','age','date','time']