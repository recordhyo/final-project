# Generated by Django 4.2.6 on 2023-11-29 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0003_alter_user_username"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="has_stb",
        ),
        migrations.AddField(
            model_name="user",
            name="stbnumber",
            field=models.IntegerField(null=True),
        ),
    ]
