import logging
import uuid

from uuid import uuid4
from django.db import models
from authentium.apps.base.models.base import ModelAbstractBase
from authentium.apps.account.models.user import ModelAccountUser
from authentium.apps.base.utility.qr_code import qr_code_generator
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw
from django.db.models.deletion import CASCADE


logger = logging.getLogger(__name__)


# ------------------------------------------------------------------------------
# ModelProduct
# ------------------------------------------------------------------------------
class ModelProduct(ModelAbstractBase):
    """
    Stores authentication information about a user of the system.
    """

    uid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        help_text="Unique identification number for the product."
    )

    user = models.ForeignKey(
        ModelAccountUser,
        related_name="user_product",
        on_delete=CASCADE,
        help_text="The user associated with this product.",
        null=True
    )

    product_name = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text="Name of the product."
    )

    product_description = models.CharField(
        max_length=500,
        null=True,
        blank=True,
        help_text="Description of the product."
    )

    front_image = models.ImageField(
        upload_to='products/',
        null=True,
        blank=True,
        help_text="Front image of the product"
    )

    back_image = models.ImageField(
        upload_to='products/',
        null=True,
        blank=True,
        help_text="Back image of the product"
    )

    qr_code = models.ImageField(
        upload_to='qr_codes',
        null=True,
        blank=True,
        help_text="QR code for the product"
    )

    product_price = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text="Price of the product."
    )

    # -------------------------------------------------------------------------
    # Meta
    # -------------------------------------------------------------------------
    class Meta:

        db_table = "product"
        verbose_name = "Product"
        verbose_name_plural = "Products"

    # ---------------------------------------------------------------------------
    # __str__
    # ---------------------------------------------------------------------------
    def __str__(self):
        """
        Returns the string representation of the user object.
        """

        return self.product_name

    
    #  ---------------------------------------------------------------
    # generate_qr_code
    #  ---------------------------------------------------------------
    def generate_qr_code(self, info):

        img = qr_code_generator(info)

        canvas = Image.new('RGB', (340, 340), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(img)
        fname = str(uuid.uuid1()) + '.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')

        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()

        self.qr_code = "qr_codes/" + fname
        self.save()

