# Generated by Django 4.2 on 2023-05-27 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_alter_projects_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='name',
            field=models.CharField(default='NOT UPDATED', max_length=40),
        ),
    ]
