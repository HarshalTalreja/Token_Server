# Generated by Django 2.2.5 on 2020-01-26 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('token_app', '0007_auto_20200126_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='updated_at',
            field=models.DateTimeField(null=True),
        ),
    ]
