# Generated by Django 5.1 on 2024-09-04 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0004_remove_account_image_account_avatar"),
    ]

    operations = [
        migrations.AlterField(
            model_name="account",
            name="avatar",
            field=models.ImageField(
                default="/accounts/avatar/avatar.png", upload_to="accounts/avatar/"
            ),
        ),
    ]
