import logging

from authentium.apps.account.models.product import ModelProduct
from django.views.generic.base import TemplateView
import uuid 
from authentium.apps.base.utility.qr_code import qr_code_generator
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw
from authentium.settings import BASE_URL
from django.views.generic.detail import DetailView
from authentium.apps.account.models.order import ModelOrder
from django.core.exceptions import ObjectDoesNotExist

logger = logging.getLogger(__name__)

 
#-------------------------------------------------------------------------------
# ViewOrderConsignment
#-------------------------------------------------------------------------------
class ViewOrderConsignment(DetailView):
    """
    Use this view to delete the note.
    """
    model = ModelOrder
    template_name = 'account/order-consignment.html'

    #---------------------------------------------------------------------------
    # get_context_data
    #---------------------------------------------------------------------------
    def get_context_data(self, **kwargs):
        
        context = DetailView.get_context_data(self, **kwargs)
        
        try:
            order=ModelOrder.objects.get(
                id=self.kwargs['pk']
            )

            if not order.qr_code:
                order.generate_qr_code(order.uid)

            context['qr_code'] = BASE_URL + "media/" +str(order.qr_code)

        except ObjectDoesNotExist:
            context['qr_code']=''
        
        return context

    