# Generated by Django 4.1.3 on 2022-11-08 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("empresa", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="vagas",
            name="empresa",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="empresa.empresa",
            ),
        ),
    ]
