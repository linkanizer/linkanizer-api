# Generated by Django 3.0 on 2020-01-03 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("linkanizer", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(name="link", options={"ordering": ("order",)},),
        migrations.AddField(
            model_name="link", name="order", field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name="list", name="order", field=models.IntegerField(default=1),
        ),
        migrations.AlterIndexTogether(name="link", index_together={("list", "order")},),
    ]
