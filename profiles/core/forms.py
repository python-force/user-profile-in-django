from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.hashers import check_password
from bootstrap_datepicker_plus import DatePickerInput
from zxcvbn_password import zxcvbn
from zxcvbn_password.fields import PasswordField, PasswordConfirmationField
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
            'city',
            'state',
            'country_of_residence',
            'favorite_animal',
            'hobby',
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
    new_password1 = PasswordField()
    new_password2 = PasswordConfirmationField(confirm_with="new_password1")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        help_text = "<ul>" \
                    "<li>Your password must not be the same as the current password</li>" \
                    "<li>Your password can't be too similar to your other personal information</li>" \
                    "<li>Your password must contain at least 14 characters</li>" \
                    "<li>Your password can't be a commonly used password</li>" \
                    "<li>Your password can't be entirely numeric</li>" \
                    "<li>Your password must not be the same as the current password</li>" \
                    "<li>Your password must use of both uppercase and lowercase letters</li>" \
                    "<li>Your password must include of one or more numerical digits</li>" \
                    "<li>Your password must include of special characters, such as @, #, $</li>" \
                    "</ul>"
        self.fields['new_password1'].help_text = help_text

        print(self.user.profile.first_name.lower())
        print(self.user.profile.last_name.lower())

    class Meta:
        fields = [
            'old_password',
            'new_password1',
            'new_password2',
        ]


    def clean(self):
        cleaned_data = super().clean()

        confirm_password = cleaned_data.get('old_password')
        if not check_password(confirm_password, self.user.password):
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

        first_name = self.user.profile.first_name.lower()
        last_name = self.user.profile.last_name.lower()

        if first_name in new_password1.lower():
            raise forms.ValidationError('Password contains your first name or last name.')

        if last_name in new_password1.lower():
            raise forms.ValidationError('Password contains your first name or last name.')

