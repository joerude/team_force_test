# Generated by Django 4.0.4 on 2022-05-20 19:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("candidates", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="skill",
            name="profile",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="profile_id",
                to="candidates.profile",
            ),
            preserve_default=False,
        ),
    ]
