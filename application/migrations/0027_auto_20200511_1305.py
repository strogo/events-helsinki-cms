# Generated by Django 2.2.9 on 2020-05-11 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0026_auto_20200506_1005'),
    ]

    operations = [
        migrations.AddField(
            model_name='collections',
            name='title_en',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Otsikko EN'),
        ),
        migrations.AddField(
            model_name='landingpages',
            name='title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Otsikko EN'),
        ),
    ]
