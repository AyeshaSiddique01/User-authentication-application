# Generated by Django 4.2.4 on 2023-09-06 08:01

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("user_app", "0005_profile_user_address"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Profile",
        ),
    ]