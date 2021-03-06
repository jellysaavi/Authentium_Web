import logging

from django.views.generic.detail import DetailView
from authentium.apps.account.models.product import ModelProduct
from django.contrib.auth.mixins import LoginRequiredMixin
from authentium.apps.base.utility.alogorand_balance import check_account_balance

logger = logging.getLogger(__name__)


#  ---------------------------------------------------------------
# ViewMarketPlaceCart
#  ---------------------------------------------------------------
class ViewMarketPlaceCart(LoginRequiredMixin, DetailView):
    model = ModelProduct
    template_name = 'market_place/cart.html'



    #  ---------------------------------------------------------------
    # get_context_data
    #  ---------------------------------------------------------------
    def get_context_data(self, **kwargs):

        context = DetailView.get_context_data(self, **kwargs)
        
        try:
            public_address = self.request.user.key_address
            context['public_address'] = public_address
            context['algo_balance'] = check_account_balance(public_address)
        except :
            context['algo_balance']='0'

        return context