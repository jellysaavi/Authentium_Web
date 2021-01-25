import logging
from pprint import pformat

from rest_framework import serializers 
from rest_framework.exceptions import ValidationError
from authentium.apps.account.models.user import ModelAccountUser
from authentium.apps.base.utility.misc import randomStringDigits
from authentium.apps.base.utility.emails import send_email

logger = logging.getLogger(__name__)

#  ---------------------------------------------------------------
# SerializerAccountFrogotPassword
#  ---------------------------------------------------------------
class SerializerAccountFrogotPassword(serializers.Serializer):
    """
    Serializer for forgot password.
    """

    email = serializers.EmailField()
     
    #  ---------------------------------------------------------------
    # validate_email
    #  ---------------------------------------------------------------
    def validate_email(self, email):
        """
        validate email
        """
        
        try :
            ModelAccountUser.objects.get(email=email.lower())
        except :
            raise ValidationError('email : User is not a registered user.')
        return email
          
    #  ---------------------------------------------------------------
    # save
    #  ---------------------------------------------------------------
    def save(self):
        """
        Send the verification email.
        """
        
        email=self.validated_data.get('email')
        user = ModelAccountUser.objects.get(email=email.lower())
        password = randomStringDigits(8)

        user.set_password(password)
        
        try:
            user.save()
        except:
            raise serializers.ValidationError(
                'Error updating the password.'
            )
        
        #Send email to the user
        html_template_path = "emails/forgot-password.html"
        text_template_path = "emails/forgot-password.txt"

        context_data = {
            'name': user.first_name,
            'password': password
        }

        send_email(
            'Forgot Password - Authentium',
            self.validated_data.get('email'),
            context_data,
            text_template_path,
            html_template_path
        )
        #//Send email to the user

        
        
