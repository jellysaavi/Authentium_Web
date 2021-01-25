import logging

from django.views.generic.base import TemplateView

from authentium.apps.account.models.user import ModelAccountUser
from authentium.settings import BASE_URL

logger = logging.getLogger(__name__)


#  ---------------------------------------------------------------
# ViewAccountUserQrCode
#  ---------------------------------------------------------------
class ViewAccountUserQrCode(TemplateView):
    template_name = 'account/qr-code.html'

    #  ---------------------------------------------------------------
    # get_context_data
    #  ---------------------------------------------------------------
    def get_context_data(self, **kwargs):

        context = TemplateView.get_context_data(self, **kwargs)

        code = self.request.GET.get('code')        
        
        user = ModelAccountUser.objects.get(
                uid=code
        )

        qr_code_url = BASE_URL + "media/" + str(user.qr_code)

        context['qr_code'] = qr_code_url

        return context

