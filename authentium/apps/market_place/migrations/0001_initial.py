# Generated by Django 3.1.1 on 2020-10-21 00:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelMarketPlaceProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date and time when this entry was created in the system')),
                ('updated', models.DateTimeField(auto_now=True, help_text='Date and time when the table data was last updated in the system')),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, help_text='Unique identification number for the product.', unique=True)),
                ('product_name', models.EmailField(blank=True, help_text='Name of the product.', max_length=255, null=True)),
                ('product_description', models.EmailField(blank=True, help_text='Description of the product.', max_length=500, null=True)),
                ('front_image', models.ImageField(blank=True, help_text='Front image of the product', null=True, upload_to='products/')),
                ('back_image', models.ImageField(blank=True, help_text='Back image of the product', null=True, upload_to='products/')),
                ('qr_code', models.ImageField(blank=True, help_text='QR code for the product', null=True, upload_to='qr_codes')),
                ('product_price', models.EmailField(blank=True, help_text='Price of the product.', max_length=255, null=True)),
                ('user', models.OneToOneField(help_text='The user associated with this product.', on_delete=django.db.models.deletion.CASCADE, related_name='user_product', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'MarketPlaceProduct',
                'verbose_name_plural': 'MarketPlaceProducts',
                'db_table': 'market_place_product',
            },
        ),
    ]
