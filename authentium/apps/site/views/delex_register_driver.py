import logging
from django.views.generic.base import TemplateView

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------
# ViewSiteDelexRegisterDriver
# ---------------------------------------------------------------
class ViewSiteDelexRegisterDriver(TemplateView):
    
    template_name = 'site/delex-register-driver.html'