# Generated by Django 3.2.5 on 2021-07-26 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("site", "0032_gift_card_settings"),
    ]

    operations = [
        migrations.AddField(
            model_name="sitesettings",
            name="reserve_stock_duration_minutes",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
