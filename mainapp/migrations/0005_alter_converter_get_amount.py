# Generated by Django 4.1.1 on 2022-10-02 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_alter_converter_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='converter',
            name='get_amount',
            field=models.FloatField(blank=True, null=True, verbose_name='Мы получаем'),
        ),
    ]
