# Generated by Django 4.2 on 2023-05-26 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tech_stacks',
            name='stack_logo',
            field=models.CharField(max_length=1000),
        ),
    ]
