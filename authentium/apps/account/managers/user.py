import logging

from django.contrib.auth.models import BaseUserManager
from django.utils import timezone

from oauth2_provider.models import AccessToken
from oauth2_provider.models import RefreshToken
from oauth2_provider.settings import oauth2_settings
from oauthlib import common
from datetime import timedelta
from authentium.settings import BASE_URL

logger = logging.getLogger(__name__)


#  ---------------------------------------------------------------
# ManagerAccountUser
#  ---------------------------------------------------------------
class ManagerAccountUser(BaseUserManager):
    """
    Provides manager methods for the user model.
    """

    #  ---------------------------------------------------------------
    # create_user
    #  ---------------------------------------------------------------
    def create_user(self, email, **kwargs):
        """
        This method creates a new user and its associated profile(empty) 
        that can be updated whenever required.
        """
        
        if not email:
            raise ValueError('Users must have a valid email address...')
        
        try:
            password = kwargs.pop('password')
        except KeyError:
            logger.warning("Password for user %s not supplied", email)
            password = ''
        
        user = self.model(email=self.normalize_email(email), **kwargs)
        
        # update user password
        user.set_password(password)

        user.is_active=True
        
        # save the new user
        user.save(using=self._db)
        
        return user
    
    #  ---------------------------------------------------------------
    # create_superuser
    #  ---------------------------------------------------------------
    def create_superuser(self, email, password):
        """
        This method creates a superuser for the system.
        It takes following arguments:
        1) email - email of superuser (required)
        2) password - strong password of superuser (required)
        3) first_name - first name of the superuser (optional)
        4) last_name - last name of superuser (optional)
        """
        
        logger.info('Creating superuser with email %s', email)
        
        user = self.create_user(
            email=email,
            password=password,
            is_staff=True,
            is_superuser=True,
            is_active=True
        )

        logger.info('Superuser %s successfully created!', user)
        
        return user

    #  ---------------------------------------------------------------
    # generate_access_token
    #  ---------------------------------------------------------------
    def generate_access_token(self, user, request, application):
        """
        Generate a valid Oauth2 Access Token, login user and return JSON 
        resonse.
        """

        # keep here for circular imports
        from authentium.apps.account.api.serializers.user import \
            SerializerAccountUser
        
        expires = timezone.now() + timedelta(
            seconds=oauth2_settings.ACCESS_TOKEN_EXPIRE_SECONDS
        )
        
        # generate the access token
        access_token = AccessToken(
            user=user,
            scope='',
            expires=expires,
            token=common.generate_token(),
            application=application
        )
        access_token.save()
        
        # generate the refresh token
        refresh_token = RefreshToken(
            user=user,
            token=common.generate_token(),
            application=application,
            access_token=access_token
        )
        refresh_token.save()        
        
        # manually login user after generating access token
        user.auto_login(request)

        qr_code_path = BASE_URL + "media/" + str(user.qr_code)
        
        return {
            'oauth_response': {
                'access_token': access_token.token,
                'refresh_token': refresh_token.token,
                'token_type': 'Bearer',
            },
            'user': SerializerAccountUser(user).data,
            'qr_code_path': qr_code_path,
            'authenticated': request.user.is_authenticated 
        }
    
    #  ---------------------------------------------------------------
    # register_user
    #  ---------------------------------------------------------------
    def register_user(self, user_data):
        
        logger.debug(
            'Attempting to create a user with data'
        )

        # create the user
        user_email = user_data.pop('email')
        user = self.create_user(user_email, **user_data)

        return user
    
    
