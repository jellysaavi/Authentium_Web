import logging

from django import forms
from authentium.apps.account.models.product import ModelProduct
from django.forms.models import ModelForm

logger = logging.getLogger(__name__)

#  ---------------------------------------------------------------
# FormProduct
#  ---------------------------------------------------------------
class FormProduct(ModelForm):
    """
    Register as Buyer at site.
    """


    product_name = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    product_description = forms.CharField(
        max_length=500,
         widget=forms.Textarea(
            attrs={
                'class': 'form-control'
            }
        )
    )

    product_price = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    front_image = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    back_image = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'class': 'form-control'
            }
        )
    )


    class Meta:
        model = ModelProduct
        fields = ['product_name', 'product_description', 'front_image', 'back_image']


    #  ---------------------------------------------------------------
    # __init__
    #  ---------------------------------------------------------------
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(FormProduct, self).__init__(*args, **kwargs)

    #  ---------------------------------------------------------------
    # save
    #  ---------------------------------------------------------------
    def save(self, commit=True):

        instance = super(FormProduct, self).save(commit=False)
        instance.save()

        instance.user = self.request.user
        instance.product_price=self.cleaned_data["product_price"]

        if commit:
            instance.save()
            instance.generate_qr_code(instance.uid)
            
        return instance