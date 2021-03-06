# Generated by Django 3.1.1 on 2020-10-07 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_modelaccountuser_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='modelaccountuser',
            name='card',
        ),
        migrations.RemoveField(
            model_name='modelaccountuser',
            name='card_holder_name',
        ),
        migrations.RemoveField(
            model_name='modelaccountuser',
            name='cvv',
        ),
        migrations.RemoveField(
            model_name='modelaccountuser',
            name='mm',
        ),
        migrations.RemoveField(
            model_name='modelaccountuser',
            name='yy',
        ),
        migrations.AddField(
            model_name='modelaccountuser',
            name='key_address',
            field=models.CharField(blank=True, help_text="What is the user's key address?", max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='modelaccountuser',
            name='user_key',
            field=models.CharField(blank=True, help_text="What is the user's key?", max_length=1000, null=True),
        ),
    ]
