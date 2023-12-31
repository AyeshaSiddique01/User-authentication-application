# Generated by Django 4.2.4 on 2023-09-06 13:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user_app", "0008_profile_user_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="user_designation",
            field=models.CharField(
                default=None, help_text="Enter your designation", max_length=40
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="user_image",
            field=models.CharField(default="uploads/empty.png", max_length=500),
        ),
    ]
