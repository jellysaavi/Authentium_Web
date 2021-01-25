import logging
from django.views.generic.base import TemplateView

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------
# ViewSiteSignUp
# ---------------------------------------------------------------
class ViewSiteSignUp(TemplateView):
    
    template_name = 'site/sign-up.html'