from django import forms
from .models import Profile
from django.core.validators import MinLengthValidator

class ProfileForm(forms.ModelForm):
    bio = forms.CharField(widget=forms.Textarea, validators=[MinLengthValidator(10)])
    class Meta:
        model = Profile
        fields = [
            'first_name',
            'last_name',
            'email',
            'email_verify',
            'date_of_birth',
            'bio',
        ]

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        verify = cleaned_data.get('email_verify')

        if email != verify:
            raise forms.ValidationError('Emails do not match')