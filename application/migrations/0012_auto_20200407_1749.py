# Generated by Django 2.2.9 on 2020-04-07 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0011_auto_20200407_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landingpage',
            name='description_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='landingpage',
            name='description_fi',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='landingpage',
            name='description_sv',
            field=models.TextField(blank=True, null=True),
        ),
    ]
