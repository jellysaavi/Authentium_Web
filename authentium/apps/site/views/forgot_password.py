import logging
from django.views.generic.base import TemplateView

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------
# ViewSiteForgotPassword
# ---------------------------------------------------------------
class ViewSiteForgotPassword(TemplateView):
    
    template_name = 'site/forgot-password.html'