import logging

from rest_framework import serializers
from rest_framework.fields import SerializerMethodField


logger = logging.getLogger(__name__)


#  ---------------------------------------------------------------
# SerializerAccountVerifyPRDToken
#  ---------------------------------------------------------------
class SerializerAccountVerifyPRDToken(serializers.Serializer):
    
    """
    Register as Buyer
    """

    prd_token = serializers.UUIDField()

   
    #  ---------------------------------------------------------------
    # verfiy
    #  ---------------------------------------------------------------
    def verfiy(self):
        pass

