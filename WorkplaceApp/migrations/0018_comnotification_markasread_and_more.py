# Generated by Django 4.1.5 on 2023-01-30 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WorkplaceApp', '0017_remove_comnotification_id_remove_message_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comnotification',
            name='MarkAsRead',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='stunotification',
            name='MarkAsRead',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]
