# Generated by Django 4.2.7 on 2023-12-03 00:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("edc_rx", "0002_rxmodificationreasons_extra_value_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="rxmodificationreasons",
            options={
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "export",
                    "import",
                ),
                "verbose_name": "Treatment Modification Reasons",
                "verbose_name_plural": "Treatment Modification Reasons",
            },
        ),
        migrations.AlterModelOptions(
            name="rxmodifications",
            options={
                "default_permissions": (
                    "add",
                    "change",
                    "delete",
                    "view",
                    "export",
                    "import",
                ),
                "verbose_name": "Treatment Modifications",
                "verbose_name_plural": "Treatment Modifications",
            },
        ),
        migrations.RemoveIndex(
            model_name="rxmodificationreasons",
            name="edc_rx_rxmo_id_b5f2cd_idx",
        ),
        migrations.RemoveIndex(
            model_name="rxmodifications",
            name="edc_rx_rxmo_id_e9eb45_idx",
        ),
        migrations.AlterField(
            model_name="rxmodificationreasons",
            name="display_index",
            field=models.IntegerField(
                default=0,
                help_text="Index to control display order if not alphabetical, not required",
                verbose_name="display index",
            ),
        ),
        migrations.AlterField(
            model_name="rxmodificationreasons",
            name="display_name",
            field=models.CharField(
                help_text="(suggest 40 characters max.)",
                max_length=250,
                unique=True,
                verbose_name="Name",
            ),
        ),
        migrations.AlterField(
            model_name="rxmodificationreasons",
            name="name",
            field=models.CharField(
                help_text="This is the stored value, required",
                max_length=250,
                unique=True,
                verbose_name="Stored value",
            ),
        ),
        migrations.AlterField(
            model_name="rxmodifications",
            name="display_index",
            field=models.IntegerField(
                default=0,
                help_text="Index to control display order if not alphabetical, not required",
                verbose_name="display index",
            ),
        ),
        migrations.AlterField(
            model_name="rxmodifications",
            name="display_name",
            field=models.CharField(
                help_text="(suggest 40 characters max.)",
                max_length=250,
                unique=True,
                verbose_name="Name",
            ),
        ),
        migrations.AlterField(
            model_name="rxmodifications",
            name="name",
            field=models.CharField(
                help_text="This is the stored value, required",
                max_length=250,
                unique=True,
                verbose_name="Stored value",
            ),
        ),
        migrations.AddIndex(
            model_name="rxmodificationreasons",
            index=models.Index(fields=["name"], name="edc_rx_rxmo_name_b72a47_idx"),
        ),
        migrations.AddIndex(
            model_name="rxmodificationreasons",
            index=models.Index(
                fields=["display_index", "display_name"],
                name="edc_rx_rxmo_display_61d256_idx",
            ),
        ),
        migrations.AddIndex(
            model_name="rxmodifications",
            index=models.Index(fields=["name"], name="edc_rx_rxmo_name_28fadc_idx"),
        ),
        migrations.AddIndex(
            model_name="rxmodifications",
            index=models.Index(
                fields=["display_index", "display_name"],
                name="edc_rx_rxmo_display_81abb3_idx",
            ),
        ),
    ]
