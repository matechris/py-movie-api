# Generated by Django 4.1.3 on 2022-11-15 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cinema", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="movie",
            name="duration",
            field=models.IntegerField(default=120),
            preserve_default=False,
        ),
    ]
