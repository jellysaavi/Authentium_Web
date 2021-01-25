import logging
from django.views.generic.base import TemplateView

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------
# ViewSiteDelexRegister
# ---------------------------------------------------------------
class ViewSiteDelexRegister(TemplateView):
    
    template_name = 'site/delex-register.html'