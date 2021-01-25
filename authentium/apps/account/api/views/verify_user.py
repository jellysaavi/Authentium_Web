import logging
import json
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from authentium.apps.account.api.serializers.verify_user import SerializerAccountVerifyUser

logger = logging.getLogger(__name__)


#---------------------------------------------------------------
# ViewAPIAccountVerifyUser
#---------------------------------------------------------------
class ViewAPIAccountVerifyUser(APIView):
    """
    API view to verify account user.
    """
    
    permission_classes = (AllowAny, )

    #---------------------------------------------------------------
    # post
    #---------------------------------------------------------------
    def post(self, request, *args, **kwargs):
        
        serializer = SerializerAccountVerifyUser(
            data=request.data,
            context={'request': request}
        )
        
        if serializer.is_valid():
            serializer.verfiy() 
            return Response({}, status=HTTP_200_OK)
         
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST) 