# Generated by Django 3.1.2 on 2020-11-26 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0004_auto_20201126_1553'),
    ]

    operations = [
        migrations.RenameField(
            model_name='issue',
            old_name='rdate',
            new_name='issued',
        ),
        migrations.AddField(
            model_name='issue',
            name='returndate',
            field=models.CharField(default='', max_length=40),
        ),
    ]
