import logging

from django.views.generic.edit import FormView
from django.urls.base import reverse_lazy
from authentium.apps.site.forms.buyer_sign_up import FormSiteBuyerSignUp

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------
# ViewSiteBuyerSignUp
# ---------------------------------------------------------------
class ViewSiteBuyerSignUp(FormView):
    
    template_name = 'site/buyer-sign-up.html'
    success_url = reverse_lazy('site:register-thanks')
    form_class = FormSiteBuyerSignUp


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
    

    
    

    
