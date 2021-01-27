# Generated by Django 3.1.2 on 2020-11-24 17:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Book', '0002_auto_20201118_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='Issue_To',
            field=models.CharField(default='None', max_length=40),
        ),
        migrations.AlterField(
            model_name='book',
            name='Quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='book',
            name='Status',
            field=models.BooleanField(default=True),
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Book.book')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]