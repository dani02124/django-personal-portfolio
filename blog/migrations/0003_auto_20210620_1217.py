# Generated by Django 3.2.2 on 2021-06-20 07:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210619_2043'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogproject',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='blogproject',
            name='description',
            field=models.CharField(max_length=250),
        ),
    ]
