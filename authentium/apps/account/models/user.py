import logging

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.contrib.auth import login

from authentium.apps.base.models.base import ModelAbstractBase
from authentium.apps.account.managers.user import ManagerAccountUser
from authentium.apps.base.utility.algorand import create_algorand_account
from authentium.apps.base.utility.qr_code import qr_code_generator
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw
from uuid import uuid4
import uuid
from authentium.apps.base.utility.misc import random_digits
from django.core.exceptions import ObjectDoesNotExist

logger = logging.getLogger(__name__)


# ------------------------------------------------------------------------------
# ModelAccountUser
# ------------------------------------------------------------------------------
class ModelAccountUser(AbstractBaseUser, ModelAbstractBase, PermissionsMixin):
    """
    Stores authentication information about a user of the system.
    """

    CURRENCY_CHOICES = (
        ('fiat', 'Fiat'),
        ('auth', 'Auth'),
    )
 
    TYPE_CHOICES = (
        ('buyer', 'Buyer'),
        ('seller', 'Seller'),
        ('driver', 'Driver'),
    )

    uid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        help_text="Unique identification number for the user."
    )

    email = models.EmailField(
        max_length=255,
        unique=True,
        help_text="Email of the user."
    )

    phone_number = models.CharField(
        max_length=60,
        null=True,
        blank=True,
        help_text="What is the user's phone number?"
    )

    first_name = models.CharField(
        max_length=60,
        null=True,
        blank=True,
        help_text="What is the user's first name?"
    )

    last_name = models.CharField(
        max_length=60,
        null=True,
        blank=True,
        help_text="What is the user's last name?"
    )

    country = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        help_text="What is the user's country?"
    )

    city = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        help_text="What is the user's city?"
    )

    currency = models.CharField(
        max_length=60,
        choices=CURRENCY_CHOICES,
        default=CURRENCY_CHOICES[0][0],
        help_text="What is the user's currency?"
    )

    user_type = models.CharField(
        max_length=60,
        choices=TYPE_CHOICES,
        default=TYPE_CHOICES[0][0],
        help_text="What is the user's role?"
    )

    key_address = models.CharField(
        max_length=1000,
        null=True,
        blank=True,
        help_text="What is the user's key address?"
    )

    user_key = models.CharField(
        max_length=1000,
        null=True,
        blank=True,
        help_text="What is the user's key?"
    )

    is_active = models.BooleanField(
        default=False,
        help_text="Is the user active?"
    )

    is_staff = models.BooleanField(
        default=False,
        help_text="Is the user as a staff member?"
    )

    is_superuser = models.BooleanField(
        default=False,
        help_text="Is the user a super user?"
    )

    qr_code = models.ImageField(
        upload_to='qr_codes',
        null=True,
        blank=True,
        help_text="QR code for the user"
    )

    short_url = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text="What is the short url for the user."
    )

    objects = ManagerAccountUser()

    USERNAME_FIELD = 'email'

    # -------------------------------------------------------------------------
    # Meta
    # -------------------------------------------------------------------------
    class Meta:

        db_table = "account_user"
        verbose_name = "User"
        verbose_name_plural = "Users"

    # ---------------------------------------------------------------------------
    # __str__
    # ---------------------------------------------------------------------------
    def __str__(self):
        """
        Returns the string representation of the user object.
        """

        return self.email

    #  ---------------------------------------------------------------
    # auto_login
    #  ---------------------------------------------------------------
    def auto_login(self, request):
        """
        A shortcut to auto login in a user, without using the user's password.
        """

        self.backend = 'django.contrib.auth.backends.ModelBackend'
        login(request, self)

    #  ---------------------------------------------------------------
    # create_algorand_account
    #  ---------------------------------------------------------------
    def create_algorand_account(self):

        private_key, public_address = create_algorand_account()

        self.key_address = public_address
        self.user_key = private_key
        self.save()

    #  ---------------------------------------------------------------
    # generate_qr_code
    #  ---------------------------------------------------------------
    def generate_qr_code(self, info):

        img = qr_code_generator(info)

        canvas = Image.new('RGB', (340, 340), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(img)
        fname = str(uuid.uuid1())  + '.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')

        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()

        self.qr_code = "qr_codes/" + fname
        self.save()

        return fname
    
    #  ---------------------------------------------------------------
    # create_short_url
    #  ---------------------------------------------------------------
    def create_short_url(self):
        try:
            short_url = str(random_digits(6))
            ModelAccountUser.objects.get(short_url=short_url)
            self.create_short_url()
        except ObjectDoesNotExist:
            self.short_url = short_url
            self.save()
        
        return short_url
        
