import logging

from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from authentium.settings import BASE_URL
from authentium.apps.account.models.order import ModelOrder
from authentium.apps.base.utility.alogorand_balance import check_account_balance

logger = logging.getLogger(__name__)


#  ---------------------------------------------------------------
# ViewAccountDashboard
#  ---------------------------------------------------------------
class ViewAccountDashboard(LoginRequiredMixin, TemplateView):
    template_name = 'account/dashboard.html'

    #  ---------------------------------------------------------------
    # get_context_data
    #  ---------------------------------------------------------------
    def get_context_data(self, **kwargs):

        context = TemplateView.get_context_data(self, **kwargs)

        orders = ModelOrder.objects.filter(
            seller=self.request.user
        )

        context['orders'] = orders

        context['qr_code'] = BASE_URL + "media/" + str(self.request.user.qr_code)

        public_address = self.request.user.key_address
        context['public_address'] = public_address
        context['algo_balance'] = check_account_balance(public_address)

        return context
