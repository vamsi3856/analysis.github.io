# Generated by Django 4.0.6 on 2022-12-06 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sheetapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productdetail',
            name='machine',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sheetapp.machine'),
        ),
    ]