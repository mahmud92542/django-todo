# Generated by Django 3.1.6 on 2021-02-06 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0002_auto_20210206_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companydeptuser',
            name='compid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.company'),
        ),
    ]