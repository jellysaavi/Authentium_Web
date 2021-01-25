import logging

from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from authentium.apps.account.models.order import ModelOrder

logger = logging.getLogger(__name__)

#  ---------------------------------------------------------------
# ViewProductList
#  ---------------------------------------------------------------
class ViewOrderList(LoginRequiredMixin, ListView):
    model = ModelOrder
    context_object_name = 'orders'
    template_name = 'account/order-list.html'

    #  ---------------------------------------------------------------
    # get_queryset
    #  ---------------------------------------------------------------
    def get_queryset(self):

        return self.model.objects.filter(
            seller=self.request.user
        )