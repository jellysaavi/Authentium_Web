import logging

from authentium.apps.account.models.product import ModelProduct
from django.views.generic.list import ListView
from authentium.apps.base.utility.alogorand_balance import check_account_balance

logger = logging.getLogger(__name__)


#  ---------------------------------------------------------------
# ViewMarketPlace
#  ---------------------------------------------------------------
class ViewMarketPlace(ListView):
    model = ModelProduct
    context_object_name = 'products'
    template_name = 'market_place/market-place.html'


    #  ---------------------------------------------------------------
    # get_context_data
    #  ---------------------------------------------------------------
    def get_context_data(self, **kwargs):

        context = ListView.get_context_data(self, **kwargs)

        try:
            public_address = self.request.user.key_address
            context['public_address'] = public_address
            context['algo_balance'] = check_account_balance(public_address)
        except :
            context['algo_balance']='0'

        return context