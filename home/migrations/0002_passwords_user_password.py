# Generated by Django 3.1.1 on 2020-09-28 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='passwords',
            name='user_password',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
