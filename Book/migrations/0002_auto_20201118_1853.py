# Generated by Django 3.1.2 on 2020-11-18 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=40)),
                ('Edition', models.DecimalField(blank=True, decimal_places=2, max_digits=6)),
                ('Author', models.CharField(default='None', max_length=40)),
                ('Description', models.TextField(default='TYPE YOUR DESCRIPTION', null=True)),
                ('Quantity', models.IntegerField(blank=True)),
                ('Issue_To', models.TextField(default='None', null=True)),
                ('Status', models.TextField(default='Available', null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Books',
        ),
    ]