# Generated by Django 4.1.1 on 2022-10-02 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='converter',
            name='get_amount',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Мы получаем'),
        ),
    ]
