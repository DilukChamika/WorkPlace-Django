# Generated by Django 4.1.5 on 2023-01-20 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WorkplaceApp', '0006_alter_flyerdata_updatetimestamp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flyerdata',
            old_name='comid',
            new_name='comname',
        ),
    ]