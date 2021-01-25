import logging

from rest_framework import serializers
from rest_framework.fields import SerializerMethodField


logger = logging.getLogger(__name__)


#  ---------------------------------------------------------------
# SerializerAccountAssignPRDToken
#  ---------------------------------------------------------------
class SerializerAccountAssignPRDToken(serializers.Serializer):
    
    """
    Register as Buyer
    """

    prd_token = serializers.UUIDField()
    user_uid = serializers.UUIDField()

   
    #  ---------------------------------------------------------------
    # assign
    #  ---------------------------------------------------------------
    def assign(self):
        pass

