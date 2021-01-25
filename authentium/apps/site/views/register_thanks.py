import logging
from django.views.generic.base import TemplateView

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------
# ViewSiteRegisterThanks
# ---------------------------------------------------------------
class ViewSiteRegisterThanks(TemplateView):
    
    template_name = 'site/register-thanks.html'