# Generated by Django 4.1.3 on 2022-11-09 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("empresa", "0002_alter_vagas_empresa"),
    ]

    operations = [
        migrations.AddField(
            model_name="vagas",
            name="email",
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name="vagas",
            name="nivel_experiencia",
            field=models.CharField(
                choices=[
                    ("T", "Trainee"),
                    ("J", "Júnior"),
                    ("P", "Pleno"),
                    ("S", "Sênior"),
                ],
                max_length=3,
            ),
        ),
    ]
