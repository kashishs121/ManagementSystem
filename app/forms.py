# from django import forms
# from django.contrib.auth.models import User 
# from django.contrib.auth.forms import UserCreationForm

# class RegisterForm(UserCreationForm):
#     name = forms.CharField(max_length=100,required = True,help_text='Enter the Name',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the Name'}),)
#     username = forms.CharField(max_length=200,required = True,help_text='Enter Username',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),)
#     password1 = forms.CharField(help_text='Enter Password',required = True,widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),)
#     password2 = forms.CharField(required = True,help_text='Enter Password Again',widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Again'}),)
#     staff_user = forms.BooleanField(initial=True)
#     submit = forms.BooleanField(required = True,help_text='Agreed')
#     class Meta:
#         model = User
#         fields = [
#             'name', 'username','password1', 'password2', 'staff_user',
#         ]
        
# class LoginForm(forms.Form):
#     username = forms.CharField(max_length=100)
#     password = forms.CharField(max_length=100, widget=forms.PasswordInput)
#     staff_user = forms.BooleanField(initial=True)

# from django import forms 
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
# from .models import staff_user

# class SignupForm(UserCreationForm):
#     class Meta:
#         model = User 
#         fields = ['username', 'password1', 'password2']

# class LoginForm(forms.Form):
#     username = forms.CharField()
#     password = forms.CharField(widget=forms.PasswordInput)
    
# class SignupFormStaff(UserCreationForm):
#     class Meta:
#         model =  staff_user
#         fields = ['username', 'password1', 'password2']

# class LoginFormStaff(forms.Form):
#     username = forms.CharField()
#     password = forms.CharField(widget=forms.PasswordInput)