from django.db import models
from django.db.models.fields import DateTimeField


#  ---------------------------------------------------------------
# ModelPRD
#  ---------------------------------------------------------------
class ModelPRD(models.Model):
    """
    Abstract base model.
    """
    
    created = DateTimeField(
        auto_now_add=True,
        help_text="Date and time when this entry was created in the system"
    )
    
    updated = DateTimeField(
        auto_now=True,
        help_text=(
            "Date and time when the table data was last updated in the system"
        )
    )
    
    #  ---------------------------------------------------------------
    # Meta
    #  ---------------------------------------------------------------
    class Meta:
        abstract = True
