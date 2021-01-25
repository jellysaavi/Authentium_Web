import logging

from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import ValidationError
from django.forms import formsets
from django.contrib.auth import login
from authentium.apps.account.models.user import ModelAccountUser

logger = logging.getLogger(__name__)

#  ---------------------------------------------------------------
# FormSiteLogin
#  ---------------------------------------------------------------
class FormSiteLogin(formsets.Form):
    """
    User this form to authenticate and login a user.
    """
    
    email = forms.EmailField(
        max_length=255,
    )
    
    password = forms.CharField(
        max_length=255,
    )

    #  ---------------------------------------------------------------
    # __init__
    #  ---------------------------------------------------------------
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(FormSiteLogin, self).__init__(*args, **kwargs)

    
    #  ---------------------------------------------------------------
    # clean_email
    #  ---------------------------------------------------------------
    def clean_email(self):

        email = self.cleaned_data.get('email')

        if email:
            return email.lower()

        return email
    
    #  ---------------------------------------------------------------
    # clean
    #  ---------------------------------------------------------------
    def clean(self):

        invalid_message = (
            'You have entered an invalid email or password.'
        )

        try:
            user = ModelAccountUser.objects.get(
                email=self.cleaned_data.get('email')
            )
            
            if not user.check_password(self.cleaned_data.get('password')):
                raise ObjectDoesNotExist('Invalid username or password')
            
        except ObjectDoesNotExist:
            raise ValidationError(invalid_message)
        
        user = authenticate(
            self.request, 
            username=self.cleaned_data.get('email'),
            password=self.cleaned_data.get('password')
        )
        
        if not user:
            raise ValidationError(invalid_message)
        
        login(self.request, user)
        return self.cleaned_data
    