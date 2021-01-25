import logging
from django.views.generic.edit import FormView
from django.urls.base import reverse_lazy
from authentium.apps.site.forms.login import FormSiteLogin
from authentium.settings import DEFAULT_LOGIN_REDIRECT_URL
from django.shortcuts import redirect

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------
# ViewSiteLogin
# ---------------------------------------------------------------
class ViewSiteLogin(FormView):
    
    template_name = 'site/login.html'
    success_url = reverse_lazy('account:dashboard')
    form_class = FormSiteLogin


    #---------------------------------------------------------------------------
    # get_form_kwargs
    #---------------------------------------------------------------------------
    def get_form_kwargs(self):
        kwargs = FormView.get_form_kwargs(self)
        kwargs['request'] = self.request
        return kwargs

    #---------------------------------------------------------------------------
    # form_valid
    #---------------------------------------------------------------------------
    def form_valid(self, form):
        """
        Login and redirect the user to the default redirect url.
        """

        try:
            url = self.request.session['next_url'] 
        except KeyError:
            if self.request.user.user_type=='buyer':
                url= reverse_lazy('market_place:market-place')
            else :
                url = DEFAULT_LOGIN_REDIRECT_URL
        
        logger.debug('Redirecting %s to %s', self.request.user, url)

        return redirect(url)