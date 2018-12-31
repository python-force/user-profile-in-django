from bootstrap_datepicker_plus import DatePickerInput
from markdownx.fields import MarkdownxFormField
from django import forms
from .models import Profile
from django.core.validators import MinLengthValidator


class ProfileForm(forms.ModelForm):
    bio = MarkdownxFormField(validators=[MinLengthValidator(10)])
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
        widgets = {
            'date_of_birth': DatePickerInput(),  # default date-format %m/%d/%Y will be used
        }

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        verify = cleaned_data.get('email_verify')

        if email != verify:
            raise forms.ValidationError('Emails do not match')