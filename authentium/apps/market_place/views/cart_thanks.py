import logging

from django.views.generic.base import TemplateView

logger = logging.getLogger(__name__)


#  ---------------------------------------------------------------
# ViewMarketPlaceCartThanks
#  ---------------------------------------------------------------
class ViewMarketPlaceCartThanks(TemplateView):
    template_name = 'market_place/cart-thanks.html'