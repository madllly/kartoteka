# Generated by Django 4.0.3 on 2022-10-03 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название района')),
            ],
        ),
        migrations.AlterModelOptions(
            name='estate',
            options={'verbose_name': 'Картотека недвижимости', 'verbose_name_plural': 'Картотека недвижимости'},
        ),
        migrations.AddField(
            model_name='estate',
            name='floor',
            field=models.CharField(default=0, max_length=255, verbose_name='Этаж'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='estate',
            name='square_meters',
            field=models.CharField(default=2, max_length=255, verbose_name='Метраж'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='estate',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.region'),
        ),
    ]
