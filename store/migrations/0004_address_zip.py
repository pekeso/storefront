# Generated by Django 4.2.4 on 2023-08-28 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='zip',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
