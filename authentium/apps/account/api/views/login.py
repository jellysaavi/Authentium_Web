import logging

from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from authentium.apps.account.api.serializers.login import SerializerAPITokenView
from authentium.apps.account.models.user import ModelAccountUser

logger = logging.getLogger(__name__)


#  ---------------------------------------------------------------
# ViewAPIAccountLogin
#  ---------------------------------------------------------------
class ViewAPIAccountLogin(APIView):
    
    permission_classes = (AllowAny,)
    
    #  ---------------------------------------------------------------
    # post
    #  ---------------------------------------------------------------
    def post(self, request, *args, **kwargs):
        
        logger.debug('Attempting to login a user.')
        
        serializer = SerializerAPITokenView(data=request.data)
        
        if serializer.is_valid():
            response = ModelAccountUser.objects.generate_access_token(
                serializer.user, request, serializer.application
            )
            return Response(response, status=HTTP_200_OK)
        
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
