# Generated by Django 5.0.6 on 2024-05-13 18:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("publications", "0002_alter_publication_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="publication",
            name="caption",
            field=models.ImageField(blank=True, upload_to="uploads/"),
        ),
    ]