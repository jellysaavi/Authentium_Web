from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from authentium.apps.account.models.user import ModelAccountUser


#  ---------------------------------------------------------------
# FormAccountUserChange
#  ---------------------------------------------------------------
class FormAccountUserChange(forms.ModelForm):
    """
    Form used for updating user information. Includes all the fields in
    the user model, but replaces the password field with admin's
    password hash display field.
    """
    
    password = ReadOnlyPasswordHashField(
        label= ("Password"),
        help_text= (
            "Raw passwords are not stored, so there is no way to see this "
            "user's password, but you can change the password using "
            "<a href=\"../password/\">this form</a>."
        )
    )

    #  ---------------------------------------------------------------
    # Meta
    #  ---------------------------------------------------------------
    class Meta:
        model = ModelAccountUser
        fields = [
            'email', 'first_name', 'last_name', 'is_staff', 'is_superuser', 
            'is_active', 'password'
        ]

    #  ---------------------------------------------------------------
    # clean_password
    #  ---------------------------------------------------------------
    def clean_password(self):
        
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        
        return self.initial["password"]
