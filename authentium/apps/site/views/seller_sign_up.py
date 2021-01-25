import logging

from django.views.generic.edit import FormView
from django.urls.base import reverse_lazy
from authentium.apps.site.forms.seller_sign_up import FormSiteSellerSignUp

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------
# ViewSiteSellerSignUp
# ---------------------------------------------------------------
class ViewSiteSellerSignUp(FormView):
    
    template_name = 'site/seller-sign-up.html'
    success_url = reverse_lazy('site:register-thanks')
    form_class = FormSiteSellerSignUp


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

        form.create()
        return FormView.form_valid(self, form)
    