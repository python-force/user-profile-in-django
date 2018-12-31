from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.hashers import check_password
from bootstrap_datepicker_plus import DatePickerInput
from markdownx.fields import MarkdownxFormField
from django import forms
from .models import Profile
from django.core.validators import MinLengthValidator
from django.shortcuts import get_object_or_404


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


class CustomChangePasswordForm(PasswordChangeForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['new_password2'].help_text = ''

    class Meta:
        fields = [
            'old_password',
            'new_password1',
            'new_password2',
        ]


    def clean(self):
        cleaned_data = super().clean()

        confirm_password = cleaned_data.get('old_password')
        if not check_password(confirm_password, [MISSING VARIABLE]):
            raise forms.ValidationError('That is not the old password')

        new_password1 = cleaned_data.get('new_password1')

        if len(new_password1) < 14:
            raise forms.ValidationError('Password is too short')

        characters = set(new_password1)

        lower = any(letter.islower() for letter in characters)
        upper = any(letter.isupper() for letter in characters)
        digit = any(letter.isdigit() for letter in characters)

        if not upper:
            raise forms.ValidationError('Password has no upper characters')

        if not lower:
            raise forms.ValidationError('Password has no lower characters')

        if not digit:
            raise forms.ValidationError('Password has no numerical character')


        special_characters = ["@", "#", "$"]
        check = False
        for character in special_characters:
            if character in new_password1:
                check = True

        if not check:
            raise forms.ValidationError('Password has no special characters, such as @, #, $.')



