import logging
import uuid

from django.db import models
from authentium.apps.base.models.base import ModelAbstractBase
from authentium.apps.account.models.user import ModelAccountUser
from django.db.models.deletion import CASCADE
from authentium.apps.account.models.product import ModelProduct
from authentium.apps.base.utility.qr_code import qr_code_generator
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw

logger = logging.getLogger(__name__)


# ------------------------------------------------------------------------------
# ModelOrder
# ------------------------------------------------------------------------------
class ModelOrder(ModelAbstractBase):
    """
    Stores authentication information about a user of the system.
    """

    uid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        help_text="Unique identification number for the order."
    )

    product_info_id = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text="Name of the order product."
    )

    buyer = models.ForeignKey(
        ModelAccountUser,
        on_delete=CASCADE,
        related_name="order_buyer",
        help_text="The buyer associated with this order.",
        null=True
    )

    product = models.ForeignKey(
        ModelProduct,
        related_name="order_products",
        on_delete=CASCADE,
        help_text="The product of the order.",
        null=True
    )

    qr_code = models.ImageField(
        upload_to='qr_codes',
        null=True,
        blank=True,
        help_text="QR code for the order"
    )

    seller = models.ForeignKey(
        ModelAccountUser,
        on_delete=CASCADE,
        related_name="order_seller",
        help_text="The seller associated with this order.",
        null=True
    )

    invoice_path = models.CharField(
        max_length=1000,
        null=True,
        blank=True,
        help_text="URL path of the invoice."
    )

    invoice_number = models.CharField(
        max_length=250,
        null=True,
        blank=True,
        help_text="Number of the invoice."
    )

    xero_Invoice_id = models.CharField(
        max_length=250,
        null=True,
        blank=True,
        help_text="Xero of the invoice."
    )

    xero_contact_id = models.CharField(
        max_length=250,
        null=True,
        blank=True,
        help_text="Xero Contact of the invoice."
    )

    # -------------------------------------------------------------------------
    # Meta
    # -------------------------------------------------------------------------
    class Meta:

        db_table = "market_order"
        verbose_name = "MarketOrder"
        verbose_name_plural = "MarketOrders"

    # ---------------------------------------------------------------------------
    # __str__
    # ---------------------------------------------------------------------------
    def __str__(self):
        """
        Returns the string representation of the user object.
        """

        return str(self.uid)

    #  ---------------------------------------------------------------
    # generate_qr_code
    #  ---------------------------------------------------------------
    def generate_qr_code(self, info):

        img = qr_code_generator(info)

        canvas = Image.new('RGB', (340, 340), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(img)
        fname = 'order_' + str(uuid.uuid1()) + '.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')

        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()

        self.qr_code = "qr_codes/" + fname
        self.save()

