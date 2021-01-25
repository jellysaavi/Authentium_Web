import logging

from django import forms
from django.forms.models import ModelForm
from authentium.apps.account.models.order import ModelOrder
from authentium.apps.account.models.product import ModelProduct

logger = logging.getLogger(__name__)

#  ---------------------------------------------------------------
# FormCartCheckout
#  ---------------------------------------------------------------
class FormCartCheckout(ModelForm):
    """
    Register a Order.
    """
    product_info_id = forms.CharField(
        max_length=255
    )

    class Meta:
        model = ModelOrder
        fields = ['product_info_id']


    #  ---------------------------------------------------------------
    # __init__
    #  ---------------------------------------------------------------
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(FormCartCheckout, self).__init__(*args, **kwargs)

    #  ---------------------------------------------------------------
    # save
    #  ---------------------------------------------------------------
    def save(self, commit=True):

        instance = super(FormCartCheckout, self).save(commit=False)

        product_id=self.cleaned_data["product_info_id"]
        product=ModelProduct.objects.get(
            id=product_id
        )
        
        instance.product=product
        instance.buyer=self.request.user
        instance.seller=product.user
        instance.save()
        
        