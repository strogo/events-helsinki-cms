# Generated by Django 2.2.9 on 2020-04-08 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0013_auto_20200407_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collections',
            name='box_color',
            field=models.CharField(choices=[('FOG', 'Sumu'), ('ENGEL', 'Engel'), ('COPPER', 'Kupari'), ('SUOMENLINNA', 'Suomenlinna')], max_length=255, null=True),
        ),
    ]