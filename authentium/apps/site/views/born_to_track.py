import logging
from django.views.generic.base import TemplateView

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------
# ViewSiteBornToTrack
# ---------------------------------------------------------------
class ViewSiteBornToTrack(TemplateView):
    
    template_name = 'site/born-to-track.html'