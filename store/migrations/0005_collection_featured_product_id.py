# Generated by Django 4.2.4 on 2023-08-29 10:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_address_zip'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='featured_product_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='store.product'),
        ),
    ]
