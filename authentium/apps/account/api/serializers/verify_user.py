import logging

from rest_framework import serializers
from rest_framework.fields import SerializerMethodField


logger = logging.getLogger(__name__)


#  ---------------------------------------------------------------
# SerializerAccountVerifyUser
#  ---------------------------------------------------------------
class SerializerAccountVerifyUser(serializers.Serializer):
    
    """
    Register as Buyer
    """

    user_uid = serializers.UUIDField()

   
    #  ---------------------------------------------------------------
    # verfiy
    #  ---------------------------------------------------------------
    def verfiy(self):
        pass

