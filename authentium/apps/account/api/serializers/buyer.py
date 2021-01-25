import logging

from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from authentium.apps.account.models.user import ModelAccountUser
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from authentium.apps.base.utility.emails import send_email
from authentium.settings import BASE_URL

logger = logging.getLogger(__name__)


#  ---------------------------------------------------------------
# SerializerAccountRegistrationBuyer
#  ---------------------------------------------------------------
class SerializerAccountRegistrationBuyer(serializers.Serializer):
    
    """
    Register as Buyer
    """

    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=60)
    first_name = serializers.CharField(max_length=60)
    last_name = serializers.CharField(max_length=60)
    mobile_number = serializers.CharField(max_length=30)
    country = serializers.CharField(max_length=30)
    city = serializers.CharField(max_length=30)
    uid = SerializerMethodField(required=False)

    #  ---------------------------------------------------------------
    # validate_email
    #  ---------------------------------------------------------------
    def validate_email(self, email):
        """
        Make sure emails are unique.
        """
        
        email = email.lower()
        
        try:
            ModelAccountUser.objects.get(email=email)
            raise serializers.ValidationError(
                'Email {} already exists. Please choose another one.'.format(email)
            )
        except ObjectDoesNotExist:
            return email
    
    #  ---------------------------------------------------------------
    # save
    #  ---------------------------------------------------------------
    def save(self):

        user_data = {
            'email': self.validated_data.get('email'),
            'password': self.validated_data.get('password'),
            'first_name': self.validated_data.get('first_name'),
            'last_name': self.validated_data.get('last_name'),
            'phone_number': self.validated_data.get('mobile_number'),
            'country': self.validated_data.get('country'),
            'city': self.validated_data.get('city'),
            'user_type':'buyer',
            'currency' : 'auth',
        }

        # Create user account in database
        buyer = ModelAccountUser.objects.register_user(
            user_data
        )

        # Create account in algorand
        buyer.create_algorand_account()

        # Generate short URL 
        # short_url = buyer.create_short_url()

        # Generate QR with user short URL
        # full_short_url = BASE_URL + str(short_url)
        # buyer.generate_qr_code(full_short_url)

        # Generate QR with user uid
        fname = buyer.generate_qr_code(buyer.uid)
        qr_code_path = BASE_URL + "media/qr_codes/" + fname

        
        # Send email to the user
        html_template_path = "emails/register.html"
        text_template_path = "emails/register.txt"

        context_data = {
            'name': self.validated_data.get('first_name'),
        }

        send_email(
            'Register at Authentium',
            self.validated_data.get('email'),
            context_data,
            text_template_path,
            html_template_path
        )
        # //Send email to the user
         
        return {
            'id': buyer.id,
            'qr_code_path': qr_code_path,
        }
