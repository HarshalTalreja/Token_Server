# Generated by Django 2.2.5 on 2020-01-26 09:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('token_app', '0004_auto_20200126_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alloted',
            name='state',
            field=models.CharField(choices=[('Free', 'Free'), ('Blocked', 'Blocked')], default='Blocked', max_length=20),
        ),
        migrations.AlterField(
            model_name='token',
            name='state',
            field=models.CharField(choices=[('Free', 'Free'), ('Blocked', 'Blocked')], default='Free', max_length=20),
        ),
        migrations.AlterField(
            model_name='token',
            name='updated_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
