# Generated by Django 4.1.4 on 2022-12-16 07:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("spitz", "0006_spitz_date_typesspitz_date"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="spitz",
            name="date",
        ),
        migrations.RemoveField(
            model_name="typesspitz",
            name="date",
        ),
        migrations.AddField(
            model_name="spitz",
            name="lastedit_date",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 12, 16, 12, 57, 34, 898141)
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="typesspitz",
            name="lastedit_date",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 12, 16, 12, 57, 45, 439519)
            ),
            preserve_default=False,
        ),
    ]
