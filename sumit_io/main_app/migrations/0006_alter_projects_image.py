# Generated by Django 4.2 on 2023-05-27 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_remove_projects_source_alter_projects_project_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='image',
            field=models.CharField(default='error.png', max_length=70),
        ),
    ]