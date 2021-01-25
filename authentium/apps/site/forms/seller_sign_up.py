import logging

from django import forms
from django.forms import formsets
from authentium.apps.account.models.user import ModelAccountUser
from authentium.settings import BASE_URL
from authentium.apps.base.utility.emails import send_email

logger = logging.getLogger(__name__)

#  ---------------------------------------------------------------
# FormSiteSellerSignUp
#  ---------------------------------------------------------------
class FormSiteSellerSignUp(formsets.Form):
    """
    Register as Buyer at site.
    """


    first_name = forms.CharField(
        max_length=255,
    )

    last_name = forms.CharField(
        max_length=255,
    )

    phone = forms.CharField(
        max_length=255,
    )

    city = forms.CharField(
        max_length=255,
    )

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
        super(FormSiteSellerSignUp, self).__init__(*args, **kwargs)

    # ---------------------------------------------------------------------------
    # create
    # ---------------------------------------------------------------------------
    def create(self):
        
        user_data = {
            'email': self.cleaned_data['email'],
            'password': self.cleaned_data['password'],
            'first_name': self.cleaned_data['first_name'],
            'last_name': self.cleaned_data['last_name'],
            'phone_number': self.cleaned_data['phone'],
            'country': 'US',
            'city': self.cleaned_data['city'],
            'user_type':'seller',
            'currency' : 'auth',
        }

        #Create user account in database
        seller = ModelAccountUser.objects.register_user(
            user_data
        )

        #Create account in algorand
        seller.create_algorand_account()

        # Generate short URL 
        short_url = seller.create_short_url()

        # Generate QR for user
        full_short_url = BASE_URL + str(short_url)
        seller.generate_qr_code(full_short_url)

        #Send email to the user
        html_template_path = "emails/register.html"
        text_template_path = "emails/register.txt"

        context_data = {
            'name': self.cleaned_data['first_name'],
        }

        send_email(
            'Register at Authentium',
            self.cleaned_data['email'],
            context_data,
            text_template_path,
            html_template_path
        )
        #//Send email to the user
         
        return seller
