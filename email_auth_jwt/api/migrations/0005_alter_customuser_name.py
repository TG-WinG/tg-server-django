# Generated by Django 5.0 on 2024-01-05 06:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0004_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="name",
            field=models.CharField(max_length=10, verbose_name="이름"),
        ),
    ]
