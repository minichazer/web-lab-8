# Generated by Django 4.1.3 on 2022-12-09 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("spitz", "0002_typesspitz"),
    ]

    operations = [
        migrations.AddField(
            model_name="spitz",
            name="typeS",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="spitz.typesspitz",
            ),
        ),
    ]
