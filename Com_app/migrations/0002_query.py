# Generated by Django 3.1.5 on 2021-01-24 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Com_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('que_category', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('question', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('approved', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
    ]
