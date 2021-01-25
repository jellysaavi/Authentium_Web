import logging
from django.views.generic.base import TemplateView

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------
# ViewSiteDelexThanks
# ---------------------------------------------------------------
class ViewSiteDelexThanks(TemplateView):
    
    template_name = 'site/delex-thanks.html'