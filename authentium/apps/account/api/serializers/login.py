import logging

from django.core.exceptions import ObjectDoesNotExist
from oauth2_provider.models import Application
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from authentium.apps.account.models.user import ModelAccountUser


logger = logging.getLogger(__name__)


#  ---------------------------------------------------------------
# SerializerAPITokenView
#  ---------------------------------------------------------------
class SerializerAPITokenView(serializers.Serializer):
    """
    Represents login data.
    """
    
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=30)
    client_id = serializers.CharField(max_length=500)
    
    #  ---------------------------------------------------------------
    # validate_client_id
    #  ---------------------------------------------------------------
    def validate_client_id(self, client_id):
        """
        Make sure the Oauth2 application exists
        """
        
        try:
            self.application = Application.objects.get(client_id=client_id)
        except ObjectDoesNotExist:
            raise ValidationError('Invalid Client ID')
    
    #  ---------------------------------------------------------------
    # validate
    #  ---------------------------------------------------------------
    def validate(self, attrs):
               
        try :
            email = attrs['email'].lower()
            self.user = ModelAccountUser.objects.get(email=email)
        except (ObjectDoesNotExist, AttributeError):
            raise serializers.ValidationError('Invalid email or password.')
        
        if not self.user.check_password(attrs['password']):
            raise serializers.ValidationError('Invalid email or password.')
        
        return serializers.Serializer.validate(self, attrs)
