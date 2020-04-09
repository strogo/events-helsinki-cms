# Generated by Django 2.2.9 on 2020-04-09 11:02

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailforms', '0004_add_verbose_name_plural'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('contenttypes', '0002_remove_content_type_name'),
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
        ('application', '0015_auto_20200409_0917'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CollectionsGroup',
            new_name='CollectionsFolder',
        ),
        migrations.AlterModelOptions(
            name='collectionsfolder',
            options={'verbose_name': 'Collections Folder'},
        ),
    ]
