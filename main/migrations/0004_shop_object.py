# Generated by Django 4.2.7 on 2024-02-27 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_shop_create_date_shop_description_shop_img_url_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='object',
            field=models.CharField(default='', max_length=255),
        ),
    ]