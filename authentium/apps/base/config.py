import logging

from django.apps.config import AppConfig

logger = logging.getLogger(__name__)


#  ---------------------------------------------------------------
# BaseAppConfig
#  ---------------------------------------------------------------
class BaseAppConfig(AppConfig):

    name = 'authentium.apps.base'
    label = 'base'
    verbose_name = 'Base'

