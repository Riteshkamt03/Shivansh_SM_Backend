# Generated by Django 4.2.6 on 2024-08-12 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shivansh_SM_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
