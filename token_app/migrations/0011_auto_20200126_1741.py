# Generated by Django 2.2.5 on 2020-01-26 12:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('token_app', '0010_auto_20200126_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='updated_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
