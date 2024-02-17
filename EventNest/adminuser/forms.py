from django import forms
from .models import EventDetails
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
     # Define a custom widget for the password fields
    username = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'class': 'form-control w-100 py-3', 'placeholder': 'Username'})
    )
    password = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={'class': 'form-control w-100 py-3', 'placeholder': 'Password'})
    )
    class Meta:
        model = User
        fields =['username','password']  

class AddEventForm(forms.ModelForm):
    class Meta:
        model = EventDetails
        fields ='__all__'
        exclude =['last_updated_by',]
        labels={
            'title':'TITLE',
            'description':'DESCRIPTION',
            'featured_image':'POSTER IMAGE',
            'event_date':'DATE OF EVENT',
            'start_time':'START TIME',
            'end_time':'END TIME',
            'speaker_name':'SPEAKER',
            'subject':'SUBJECT',
            'is_published':'PUBLISHED',
            'is_online':'ONLINE',
            'video_link':'VIDEO LINK',
            'seats_available':'SEATS AVAILABLE',
           
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control w-100 py-3'}),
            'description': forms.Textarea(attrs={'class': 'form-control w-100 py-3'}),
            'featured_image': forms.ClearableFileInput(attrs={'accept': 'image/*', 'class': 'form-control w-100 py-3'}),
            'event_date': forms.DateInput(attrs={'class': 'form-control w-100 py-3'}),
            'start_time': forms.TimeInput(attrs={'class': 'form-control w-100 py-3'}),
            'end_time': forms.TimeInput(attrs={'class': 'form-control w-100 py-3'}),
            'speaker_name': forms.TextInput(attrs={'class': 'form-control w-100 py-3'}),
            'subject': forms.TextInput(attrs={'class': 'form-control w-100 py-3'}),
            'is_published': forms.CheckboxInput(attrs={'class': 'form-check-input'}),  
            'is_online': forms.CheckboxInput(attrs={'class': 'form-check-input'}),  
            'video_link': forms.URLInput(attrs={'class': 'form-control w-100 py-3'}),
            'seats_available': forms.TextInput(attrs={'class': 'form-control w-100 py-3'}),
        }

       
   