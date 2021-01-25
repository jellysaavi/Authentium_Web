from django import forms

from authentium.apps.account.models.user import ModelAccountUser


#  ---------------------------------------------------------------
# FormAccountUserAdmin
#  ---------------------------------------------------------------
class FormAccountUserAdmin(forms.ModelForm):
    """
    A form used for creating new users. Includes all the required
    fields, plus a confirm_password field.
    """

    first_name = forms.CharField(
        max_length=60, required=False, 
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    last_name = forms.CharField(
        max_length=60, required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput
    )

    confirm_password = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput
    )

    email = forms.EmailField() #validates email
    
    #  ---------------------------------------------------------------
    # Meta
    #  ---------------------------------------------------------------
    class Meta:

        model = ModelAccountUser
        fields = ['email', 'first_name', 'last_name', 'is_staff', 
                  'is_superuser', 'is_active']

    #  ---------------------------------------------------------------
    # clean_confirm_password
    #  ---------------------------------------------------------------
    def clean_confirm_password(self):
        """
        This method is used to check whether both the password entries
        match or not.
        """

        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords don't match")

        return confirm_password

    
    #  ---------------------------------------------------------------
    # save
    #  ---------------------------------------------------------------
    def save(self, commit=True):
        """
        This method is used to save the user account's password as
        hashed password.
        """

        user = super().save(commit=False)
        #Updates the user's password as a hashed password
        user.set_password(self.cleaned_data["password"])

        if commit:
            user.save()

        return user
