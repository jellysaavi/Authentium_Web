import logging
import json
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from authentium.apps.account.api.serializers.buyer import SerializerAccountRegistrationBuyer
from authentium.apps.account.api.serializers.driver import SerializerAccountRegistrationDriver


logger = logging.getLogger(__name__)


#---------------------------------------------------------------
# ViewAPIAccountRegistrationDriver
#---------------------------------------------------------------
class ViewAPIAccountRegistrationDriver(APIView):
    """
    API view for driver
    """

    permission_classes = (AllowAny, )

    #---------------------------------------------------------------
    # post
    #---------------------------------------------------------------
    def post(self, request, *args, **kwargs):
        
        serializer = SerializerAccountRegistrationDriver(
            data=request.data,
            context={'request': request}
        )
        
        if serializer.is_valid():
            response = serializer.save() 
            return Response(response, status=HTTP_200_OK)
         
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)    