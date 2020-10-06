# Generated by Django 2.2.9 on 2020-09-24 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0041_auto_20200924_0816'),
    ]

    operations = [
        migrations.AddField(
            model_name='landingpages',
            name='title_and_description_color_en',
            field=models.CharField(blank=True, choices=[('BLACK', 'Black'), ('WHITE', 'White')], max_length=255, null=True, verbose_name='Tekstin väri EN'),
        ),
        migrations.AddField(
            model_name='landingpages',
            name='title_and_description_color_fi',
            field=models.CharField(blank=True, choices=[('BLACK', 'Black'), ('WHITE', 'White')], max_length=255, null=True, verbose_name='Tekstin väri FI'),
        ),
        migrations.AddField(
            model_name='landingpages',
            name='title_and_description_color_sv',
            field=models.CharField(blank=True, choices=[('BLACK', 'Black'), ('WHITE', 'White')], max_length=255, null=True, verbose_name='Tekstin väri SV'),
        ),
    ]