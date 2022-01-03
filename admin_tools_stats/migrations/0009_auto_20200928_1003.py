# Generated by Django 3.0.10 on 2020-09-28 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("admin_tools_stats", "0008_auto_20200911_1400"),
    ]

    operations = [
        migrations.AddField(
            model_name="criteriatostatsm2m",
            name="choices_based_on_time_range",
            field=models.BooleanField(
                default=False,
                help_text="Choices are not cached if this is set to true",
                verbose_name="Choices are dependend on chart time range",
            ),
        ),
        migrations.AddField(
            model_name="criteriatostatsm2m",
            name="count_limit",
            field=models.PositiveIntegerField(blank=True, default=None, null=True),
        ),
    ]
