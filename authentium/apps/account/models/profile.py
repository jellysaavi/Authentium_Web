import logging

from django.db import models
from timezone_field.fields import TimeZoneField

from authentium.apps.account.models.user import ModelAccountUser
from authentium.apps.base.models.base import ModelAbstractBase


logger = logging.getLogger(__name__)


#  ---------------------------------------------------------------
# ModelAccountProfile
#  ---------------------------------------------------------------
class ModelAccountProfile(ModelAbstractBase):
    """
    Stores profile information for a user
    """
    
    user = models.OneToOneField(
        ModelAccountUser,
        on_delete=models.CASCADE,
        related_name="profile",
        help_text="The user associated with this profile."
    )

    notification= models.BooleanField(
        default=False,
        help_text=(
            "user notification"
        )
    )

    timezone = TimeZoneField() # defaults supported 
    
    # -------------------------------------------------------------------------
    # Meta
    # -------------------------------------------------------------------------
    class Meta:

        db_table = "account_profile"
        verbose_name = "profile"
        verbose_name_plural = "Profils"

    # ---------------------------------------------------------------------------
    # __str__
    # ---------------------------------------------------------------------------
    def __str__(self):
        """
        Returns the string representation of the profile.
        """

        return self.user.email
