# Generated by Django 3.2.2 on 2021-06-27 12:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210620_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogproject',
            name='date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
