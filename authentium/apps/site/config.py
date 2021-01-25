import logging
from authentium.apps.base.config import BaseAppConfig

logger = logging.getLogger(__name__)


#  ---------------------------------------------------------------
# ConfigSite
#  ---------------------------------------------------------------
class ConfigSite(BaseAppConfig):
    
    name = 'authentium.apps.site'
    label = 'site'
    verbose_name = 'Site'
