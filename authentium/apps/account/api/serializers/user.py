import logging

from rest_framework.serializers import ModelSerializer
from authentium.apps.account.models.user import ModelAccountUser

logger = logging.getLogger(__name__)

#  ---------------------------------------------------------------
# SerializerAccountUser
#  ---------------------------------------------------------------
class SerializerAccountUser(ModelSerializer):
    """
    Resents API data for a user.
    """
    
    #  ---------------------------------------------------------------
    # Meta
    #  ---------------------------------------------------------------
    class Meta:
        model = ModelAccountUser
        fields = ('email', 'first_name', 'last_name', 'id')

