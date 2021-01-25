import logging
import json
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from authentium.apps.account.api.serializers.update_order import SerializerAccountUpdateOrder

logger = logging.getLogger(__name__)


#---------------------------------------------------------------
# ViewAPIAccountUpdateOrder
#---------------------------------------------------------------
class ViewAPIAccountUpdateOrder(APIView):
    """
    API view for seller
    """

    permission_classes = (AllowAny, )

    #---------------------------------------------------------------
    # post
    #---------------------------------------------------------------
    def post(self, request, *args, **kwargs):
        
        serializer = SerializerAccountUpdateOrder(
            data=request.data,
            context={'request': request}
        )
        
        if serializer.is_valid():
            response = serializer.save() 
            return Response(response, status=HTTP_200_OK)
         
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)    