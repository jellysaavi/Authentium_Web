import logging

from django.views.generic.edit import FormView
from django.urls.base import reverse_lazy
from authentium.apps.site.forms.driver_sign_up import FormSiteDriverSignUp

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------
# ViewSiteDriverSignUp
# ---------------------------------------------------------------
class ViewSiteDriverSignUp(FormView):
    
    template_name = 'site/driver-sign-up.html'
    success_url = reverse_lazy('site:register-thanks')
    form_class = FormSiteDriverSignUp


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
    
