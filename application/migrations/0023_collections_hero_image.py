# Generated by Django 2.2.9 on 2020-04-29 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
        ('application', '0022_auto_20200417_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='collections',
            name='hero_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='wagtailimages.Image'),
        ),
    ]