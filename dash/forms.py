from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from django import forms
from .models import Customer_db


# sign up form
class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email','password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Email Address'
        self.fields['email'].label = ''
        self.fields['email'].max_length= 50

        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['placeholder'] = 'First name'
        self.fields['first_name'].label = ''
        self.fields['first_name'].max_length= 20

        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last name'
        self.fields['last_name'].label = ''
        self.fields['last_name'].max_length= 20

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 50 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	

# add record form
class AddrecordForm(forms.ModelForm):
    class Meta:
        model = Customer_db
        fields = '__all__'

    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'First name', 'class':'form-control'}), label='')
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Last name', 'class':'form-control'}), label='')
    email = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Email', 'class':'form-control'}), label='')
    phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Phone', 'class':'form-control'}), label='')
    address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Address', 'class':'form-control'}), label='')
    city = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'City', 'class':'form-control'}), label='')
    state = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'State', 'class':'form-control'}), label='')
    zipcode = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Zipcode', 'class':'form-control'}), label='')