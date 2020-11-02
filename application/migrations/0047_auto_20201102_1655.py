# Generated by Django 2.2.9 on 2020-11-02 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0046_auto_20201014_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collections',
            name='hero_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='application.CustomImage', verbose_name='Kokoelman pääkuva'),
        ),
        migrations.AlterField(
            model_name='landingpages',
            name='hero_background_image_en',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='application.CustomImage', verbose_name='Pääkuva EN'),
        ),
        migrations.AlterField(
            model_name='landingpages',
            name='hero_background_image_fi',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='application.CustomImage', verbose_name='Pääkuva FI'),
        ),
        migrations.AlterField(
            model_name='landingpages',
            name='hero_background_image_mobile_en',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='application.CustomImage', verbose_name='Pääkuva mobiililla EN'),
        ),
        migrations.AlterField(
            model_name='landingpages',
            name='hero_background_image_mobile_fi',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='application.CustomImage', verbose_name='Pääkuva mobiililla FI'),
        ),
        migrations.AlterField(
            model_name='landingpages',
            name='hero_background_image_mobile_sv',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='application.CustomImage', verbose_name='Pääkuva mobiililla SV'),
        ),
        migrations.AlterField(
            model_name='landingpages',
            name='hero_background_image_sv',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='application.CustomImage', verbose_name='Pääkuva SV'),
        ),
        migrations.AlterField(
            model_name='landingpages',
            name='hero_top_layer_image_en',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='application.CustomImage', verbose_name='Pääkuvan päälle asettuva kuva EN'),
        ),
        migrations.AlterField(
            model_name='landingpages',
            name='hero_top_layer_image_fi',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='application.CustomImage', verbose_name='Pääkuvan päälle asettuva kuva FI'),
        ),
        migrations.AlterField(
            model_name='landingpages',
            name='hero_top_layer_image_sv',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='application.CustomImage', verbose_name='Pääkuvan päälle asettuva kuva SV'),
        ),
        migrations.AlterField(
            model_name='landingpages',
            name='social_media_image_en',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='application.CustomImage', verbose_name='Some-postauksen kuva EN'),
        ),
        migrations.AlterField(
            model_name='landingpages',
            name='social_media_image_fi',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='application.CustomImage', verbose_name='Some-postauksen kuva FI'),
        ),
        migrations.AlterField(
            model_name='landingpages',
            name='social_media_image_sv',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='application.CustomImage', verbose_name='Some-postauksen kuva SV'),
        ),
    ]
