import logging
from authentium.apps.base.config import BaseAppConfig

logger = logging.getLogger(__name__)


#  ---------------------------------------------------------------
# ConfigMarketPlace
#  ---------------------------------------------------------------
class ConfigMarketPlace(BaseAppConfig):

    name = 'authentium.apps.market_place'
    label = 'market_place'
    verbose_name = 'Market Place'
    verbose_name_plural = 'Market Place'