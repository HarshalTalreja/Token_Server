# Generated by Django 2.2.5 on 2020-01-26 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('token_app', '0009_auto_20200126_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
