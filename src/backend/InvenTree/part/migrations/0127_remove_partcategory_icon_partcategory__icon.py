# Generated by Django 4.2.11 on 2024-07-20 22:30

import common.icons
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('part', '0126_part_revision_of'),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=[],
            state_operations=[
                migrations.RenameField(
                    model_name='partcategory',
                    old_name='icon',
                    new_name='_icon',
                ),
                migrations.AlterField(
                    model_name='partcategory',
                    name='_icon',
                    field=models.CharField(blank=True, db_column='icon', help_text='Icon (optional)', max_length=100, validators=[common.icons.validate_icon], verbose_name='Icon'),
                ),
            ],
        ),
    ]