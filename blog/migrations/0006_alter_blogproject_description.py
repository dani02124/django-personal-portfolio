# Generated by Django 3.2.2 on 2021-07-02 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_blogproject_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogproject',
            name='description',
            field=models.TextField(max_length=550),
        ),
    ]
