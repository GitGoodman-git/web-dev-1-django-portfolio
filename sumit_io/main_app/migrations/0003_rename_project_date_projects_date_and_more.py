# Generated by Django 4.2 on 2023-05-27 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_tech_stacks_stack_logo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projects',
            old_name='project_date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='projects',
            old_name='project_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='projects',
            old_name='project_link',
            new_name='link',
        ),
        migrations.RemoveField(
            model_name='projects',
            name='project_name',
        ),
        migrations.AddField(
            model_name='projects',
            name='image',
            field=models.CharField(default='github', max_length=70),
        ),
        migrations.AddField(
            model_name='projects',
            name='name',
            field=models.CharField(default='', max_length=40),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tech_stacks',
            name='stack_logo',
            field=models.CharField(max_length=4000),
        ),
    ]
