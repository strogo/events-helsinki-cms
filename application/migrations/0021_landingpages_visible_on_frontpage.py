# Generated by Django 2.2.9 on 2020-04-15 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0020_auto_20200415_1244'),
    ]

    operations = [
        migrations.AddField(
            model_name='landingpages',
            name='visible_on_frontpage',
            field=models.BooleanField(default=False, verbose_name='Näytä kokoelma etusivulla'),
        ),
    ]
