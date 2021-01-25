import logging

from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from authentium.apps.account.models.user import ModelAccountUser
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from authentium.apps.base.utility.emails import send_email
from authentium.settings import BASE_URL
from authentium.apps.account.models.order import ModelOrder
from authentium.apps.base.utility.algorand_transactions import create_transactions


logger = logging.getLogger(__name__)


#  ---------------------------------------------------------------
# SerializerAccountUpdateOrder
#  ---------------------------------------------------------------
class SerializerAccountUpdateOrder(serializers.Serializer):
    
    """
    Update order
    """

    order_id = serializers.CharField(max_length=200)
    invoice_number = serializers.CharField(max_length=200)
    xero_Invoice_id = serializers.CharField(max_length=200)
    xero_contact_id = serializers.CharField(max_length=200)

    #  ---------------------------------------------------------------
    # save
    #  ---------------------------------------------------------------
    def save(self):

        try:
            order = ModelOrder.objects.get(
                id=self.validated_data.get('order_id')
            )
            
            order.invoice_number = self.validated_data.get('invoice_number')
            order.xero_Invoice_id = self.validated_data.get('xero_Invoice_id')
            order.xero_contact_id = self.validated_data.get('xero_contact_id')
            order.save()

            # Transfer the money
            amount = order.product.product_price
            from_address = order.buyer.key_address
            from_key = order.buyer.user_key
            to_address = order.seller.key_address

            logger.error("jellysaini")
            logger.error(amount)
            logger.error(from_address)
            logger.error(from_key)
            logger.error(to_address)


            create_transactions(amount, from_address, to_address, from_key)

        except ObjectDoesNotExist:
            pass
