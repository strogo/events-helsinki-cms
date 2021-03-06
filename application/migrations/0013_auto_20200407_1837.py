# Generated by Django 2.2.9 on 2020-04-07 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0012_auto_20200407_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landingpage',
            name='button_text_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Napin teksti EN'),
        ),
        migrations.AlterField(
            model_name='landingpage',
            name='button_text_fi',
            field=models.CharField(max_length=255, null=True, verbose_name='Napin teksti FI'),
        ),
        migrations.AlterField(
            model_name='landingpage',
            name='button_text_sv',
            field=models.CharField(max_length=255, null=True, verbose_name='Napin teksti SV'),
        ),
        migrations.AlterField(
            model_name='landingpage',
            name='button_url_en',
            field=models.URLField(max_length=500, null=True, verbose_name='Linkki englanninkieliselle sivulle'),
        ),
        migrations.AlterField(
            model_name='landingpage',
            name='button_url_fi',
            field=models.URLField(max_length=500, null=True, verbose_name='Linkki suomenkieliselle sivulle'),
        ),
        migrations.AlterField(
            model_name='landingpage',
            name='button_url_sv',
            field=models.URLField(max_length=500, null=True, verbose_name='Linkki ruotsinkieliselle sivulle'),
        ),
        migrations.AlterField(
            model_name='landingpage',
            name='description_en',
            field=models.TextField(blank=True, null=True, verbose_name='Selite EN'),
        ),
        migrations.AlterField(
            model_name='landingpage',
            name='description_fi',
            field=models.TextField(blank=True, null=True, verbose_name='Selite FI'),
        ),
        migrations.AlterField(
            model_name='landingpage',
            name='description_sv',
            field=models.TextField(blank=True, null=True, verbose_name='Selite SV'),
        ),
        migrations.AlterField(
            model_name='landingpage',
            name='meta_information_en',
            field=models.TextField(null=True, verbose_name='Meta tieto EN'),
        ),
        migrations.AlterField(
            model_name='landingpage',
            name='meta_information_fi',
            field=models.TextField(null=True, verbose_name='Meta tieto FI'),
        ),
        migrations.AlterField(
            model_name='landingpage',
            name='meta_information_sv',
            field=models.TextField(null=True, verbose_name='Meta tieto SV'),
        ),
        migrations.AlterField(
            model_name='landingpage',
            name='page_title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Sivun title EN'),
        ),
        migrations.AlterField(
            model_name='landingpage',
            name='page_title_fi',
            field=models.CharField(max_length=255, null=True, verbose_name='Sivun title FI'),
        ),
        migrations.AlterField(
            model_name='landingpage',
            name='page_title_sv',
            field=models.CharField(max_length=255, null=True, verbose_name='Sivun title SV'),
        ),
        migrations.AlterField(
            model_name='landingpage',
            name='title_fi',
            field=models.CharField(max_length=255, null=True, verbose_name='Otsikko FI'),
        ),
        migrations.AlterField(
            model_name='landingpage',
            name='title_sv',
            field=models.CharField(max_length=255, null=True, verbose_name='Otsikko SV'),
        ),
    ]
