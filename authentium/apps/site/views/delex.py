import logging
from django.views.generic.base import TemplateView

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------
# ViewSiteDelex
# ---------------------------------------------------------------
class ViewSiteDelex(TemplateView):
    
    template_name = 'site/delex.html'