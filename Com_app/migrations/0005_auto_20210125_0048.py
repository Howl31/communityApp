# Generated by Django 3.1.5 on 2021-01-24 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Com_app', '0004_auto_20210125_0046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='que_id',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
    ]
