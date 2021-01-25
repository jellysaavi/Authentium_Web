import logging

from django.views.generic.edit import DeleteView
from django.urls.base import reverse_lazy
from authentium.apps.account.models.product import ModelProduct


logger = logging.getLogger(__name__)

 
#-------------------------------------------------------------------------------
# ViewProductDelete
#-------------------------------------------------------------------------------
class ViewProductDelete(DeleteView):
    """
    Use this view to delete the note.
    """
    model = ModelProduct
    template_name = 'account/product-delete.html'
    success_url = reverse_lazy('account:product-list')
