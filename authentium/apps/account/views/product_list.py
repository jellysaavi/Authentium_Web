import logging

from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from authentium.apps.account.models.product import ModelProduct

logger = logging.getLogger(__name__)

#  ---------------------------------------------------------------
# ViewProductList
#  ---------------------------------------------------------------
class ViewProductList(LoginRequiredMixin, ListView):
    model = ModelProduct
    context_object_name = 'products'
    template_name = 'account/product-list.html'

    #  ---------------------------------------------------------------
    # get_queryset
    #  ---------------------------------------------------------------
    def get_queryset(self):

        return self.model.objects.filter(
            user=self.request.user
        )