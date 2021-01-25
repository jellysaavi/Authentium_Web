import logging

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from authentium.apps.account.models.profile import ModelAccountProfile
from authentium.apps.account.models.user import ModelAccountUser
from authentium.apps.account.forms.user_change import FormAccountUserChange
from authentium.apps.account.forms.user_admin import FormAccountUserAdmin

logger = logging.getLogger(__name__)


#  ---------------------------------------------------------------
# InlineAccountProfile
#  ---------------------------------------------------------------
class InlineAccountProfile(admin.StackedInline):
    """
    Manages the fields of InlineAccountProfile in the django admin section.
    """
    model = ModelAccountProfile


#  ---------------------------------------------------------------
# AdminAccountUser
#  ---------------------------------------------------------------
@admin.register(ModelAccountUser)
class AdminAccountUser(BaseUserAdmin):
    """
    Manages the fields of ModelAccountUser in the django admin section.
    """
    inlines = [InlineAccountProfile]
    form = FormAccountUserChange
    add_form = FormAccountUserAdmin

    list_display = (
        'email', 'id', 'first_name', 'phone_number',
        'is_staff', 'is_superuser', 'is_active', 'created', 'updated'
    )

    list_filter = ('is_superuser', 'is_staff', 'is_active')
    readonly_fields = ('groups', 'profile')

    fieldsets = (
        (
            None,
            {
                'fields':
                    (
                        'email', 'password', 'phone_number'
                    )
            }
        ),
        (
            'Personal info',
            {
                'fields': ('first_name', 'last_name', 'short_url', 'qr_code')
            }
        ),
        (
            'Permissions',
            {
                'fields': ('is_staff', 'is_superuser', 'is_active',)}),
        ('Groups', {'fields': ('groups',)}),
      
    )

    add_fieldsets = (
        (None,
         {
             'classes': ('wide',),
             'fields': (
                 'email', 'first_name', 'last_name', 'password',
                 'confirm_password', 'is_staff', 'is_superuser', 'is_active'
             )
         }
         ),
    )

    search_fields = ('email',)
    ordering = ('email',)

