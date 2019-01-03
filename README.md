# User Profile in Django

For this project, building a form that takes in details about a registered user and displays those details on a profile page. The profile page should only be visible once the user has logged in.The profile page should include first name, last name, email, date of birth, confirm email, short bio and the option to upload an avatar.

Set up validation for email, date of birth and the biography. The Date of Birth validation should accept three date formats: YYYY-MM-DD, MM/DD/YYYY, or MM/DD/YY. The Email validation should check if the email addresses match and are in a valid format. The bio validation should check that the bio is 10 characters or longer and properly escapes HTML formatting.

Create a "change password page" that updates the user’s password. This page will ask for current password, new password and confirm password. Set up validation which checks that the current password is valid, that the new password and confirm password fields match, and that the new password follows the following policy:

<ul>
<li>must not be the same as the current password</li>
<li>minimum password length of 14 characters.</li>
<li>must use of both uppercase and lowercase letters</li>
<li>must include of one or more numerical digits</li>
<li>must include of special characters, such as @, #, $</li>
<li>cannot contain the username or parts of the user’s full name, such as his first name</li>
</ul>

## Features

<ul>
<li>Password Strength Meter</li>
<li>Date Picker Tool for Date Field</li>
<li>Crop Photo Editor</li>
<li>Markdown for Bio Field</li>
<li>Pagedown for Bio Field</li>
<li>Extra Fields</li>
</ul>
