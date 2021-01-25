import logging
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from authentium.apps.account.models.user import ModelAccountUser

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------
# ViewSiteDelexExchange
# ---------------------------------------------------------------
class ViewSiteDelexExchange(ListView):
    model = ModelAccountUser
    context_object_name = 'exchanges'
    template_name = 'site/delex-exchange.html'

    #  ---------------------------------------------------------------
    # get_queryset
    #  ---------------------------------------------------------------
    def get_queryset(self):

        return self.model.objects.filter(
            last_name='business'
        )