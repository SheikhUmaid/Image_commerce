# Generated by Django 4.2.4 on 2023-08-06 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_customusermodel_products_purchased'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_payment_id',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_file',
            field=models.FileField(blank=True, default='', null=True, upload_to='files'),
        ),
    ]
