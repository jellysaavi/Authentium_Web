from rest_framework.serializers import ModelSerializer

from rest_framework.fields import SerializerMethodField
from authentium.apps.account.models.profile import ModelAccountProfile


#  ---------------------------------------------------------------
# SerializerAccountProfile
#  ---------------------------------------------------------------
class SerializerAccountProfile(ModelSerializer):
    """
    Resents API data for a user's profile
    """
    
    timezone = SerializerMethodField()
    
    #  ---------------------------------------------------------------
    # Meta
    #  ---------------------------------------------------------------
    class Meta:
        model = ModelAccountProfile
        fields = ('timezone', )
        
    #  ---------------------------------------------------------------
    # get_timezone
    #  ---------------------------------------------------------------
    def get_timezone(self, profile):
        return str(profile.timezone) if profile.timezone else ''
