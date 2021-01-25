import logging

from django.views.generic.detail import DetailView
from authentium.apps.account.models.order import ModelOrder
from django.core.exceptions import ObjectDoesNotExist
from authentium.settings import BASE_URL

logger = logging.getLogger(__name__)


#  ---------------------------------------------------------------
# ViewOrderMapView
#  ---------------------------------------------------------------
class ViewOrderMapView(DetailView):

    model=ModelOrder
    template_name = 'account/order-map-view.html'


    # get_context_data
    #---------------------------------------------------------------------------
    def get_context_data(self, **kwargs):
        
        context = DetailView.get_context_data(self, **kwargs)
        
        try:
            order=ModelOrder.objects.get(
                id=self.kwargs['pk']
            )
            context['qr_code'] = BASE_URL + "media/" +str(order.qr_code)
            
        except ObjectDoesNotExist:
            context['qr_code']=''
        
        return context
