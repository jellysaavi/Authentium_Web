from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls.base import reverse
from django.views.generic.base import RedirectView
from django.contrib.auth import logout


#  ---------------------------------------------------------------
# ViewAccountUserLogout
#  ---------------------------------------------------------------
class ViewAccountLogout(LoginRequiredMixin, RedirectView):
    """
    View to handle logout process.
    """
    
    permanent = False
    
    #  ---------------------------------------------------------------
    # get_redirect_url
    #  ---------------------------------------------------------------
    def get_redirect_url(self, *args, **kwargs):
        """
        Method to logout user and redirect it to the login screen.
        """
        logout(self.request)
        return reverse('site:login')