# Generated by Django 3.2.19 on 2023-05-19 06:04

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('part', '0109_auto_20230517_1048'),
        ('build', '0042_alter_build_notes'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuildLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=5, default=1, help_text='Required quantity for build order', max_digits=15, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Quantity')),
                ('bom_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='build_lines', to='part.bomitem')),
                ('build', models.ForeignKey(help_text='Build object', on_delete=django.db.models.deletion.CASCADE, related_name='build_lines', to='build.build')),
            ],
            options={
                'unique_together': {('build', 'bom_item')},
                'verbose_name': 'Build Order Line Item',
            },
        ),
    ]