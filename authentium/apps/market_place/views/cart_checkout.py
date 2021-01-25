import logging

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from authentium.apps.market_place.forms.cart_checkout import FormCartCheckout
from django.urls.base import reverse_lazy

logger = logging.getLogger(__name__)


#  ---------------------------------------------------------------
# ViewMarketPlaceCartCheckout
#  ---------------------------------------------------------------
class ViewMarketPlaceCartCheckout(LoginRequiredMixin, FormView):
    template_name = 'market_place/cart.html'
    form_class = FormCartCheckout
    success_url = reverse_lazy('market_place:cart-thanks')

    #---------------------------------------------------------------------------
    # get_form_kwargs
    #---------------------------------------------------------------------------
    def get_form_kwargs(self):
        kwargs = FormView.get_form_kwargs(self)
        kwargs['request'] = self.request
        return kwargs

    #  ---------------------------------------------------------------
    # form_valid
    #  ---------------------------------------------------------------
    def form_valid(self, form):
        form.save()
        return FormView.form_valid(self, form)