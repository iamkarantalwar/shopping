# Generated by Django 2.2.5 on 2019-11-15 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminside', '0002_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(default=1, upload_to='products/'),
            preserve_default=False,
        ),
    ]
