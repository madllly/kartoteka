# Generated by Django 4.0.3 on 2022-10-18 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_region_options_estate_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='estate',
            name='cover',
            field=models.ImageField(default=1, upload_to='images/'),
            preserve_default=False,
        ),
    ]
