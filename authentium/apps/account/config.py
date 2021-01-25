import logging
from authentium.apps.base.config import BaseAppConfig

logger = logging.getLogger(__name__)


#  ---------------------------------------------------------------
# ConfigAccount
#  ---------------------------------------------------------------
class ConfigAccount(BaseAppConfig):

    name = 'authentium.apps.account'
    label = 'account'
    verbose_name = 'Account Management'
    verbose_name_plural = 'Account Management'