import logging

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls.base import reverse_lazy
from authentium.apps.account.forms.product import FormProduct
from django.views.generic.edit import FormView

logger = logging.getLogger(__name__)


#  ---------------------------------------------------------------
# ViewProduct
#  ---------------------------------------------------------------
class ViewProduct(LoginRequiredMixin, FormView):
    template_name = 'account/product.html'
    success_url = reverse_lazy('account:product-list')
    form_class = FormProduct

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