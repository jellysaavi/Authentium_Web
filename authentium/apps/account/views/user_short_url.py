import logging
from django.views.generic.base import RedirectView
from authentium.apps.account.models.user import ModelAccountUser
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import Http404
from django.urls.base import reverse

logger = logging.getLogger(__name__)


#  ---------------------------------------------------------------
# ViewAccountShortUrl
#  ---------------------------------------------------------------
class ViewAccountShortUrl(RedirectView):
    
    #  ---------------------------------------------------------------
    # get_redirect_url
    #  ---------------------------------------------------------------
    def get_redirect_url(self, *args, **kwargs):
        
        short_url = self.kwargs['path']

        try:
            user = ModelAccountUser.objects.get(
                short_url=short_url
            )

            #Creating the log URL for the user.
            url = reverse('account:user-qr-code') + "?code=" + str(user.uid) 
            return url

        except ObjectDoesNotExist:
            raise Http404('Invalid short URL.')

