# Generated by Django 3.1.1 on 2020-10-05 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelaccountuser',
            name='country',
            field=models.CharField(blank=True, help_text="What is the user's country?", max_length=200, null=True),
        ),
    ]
