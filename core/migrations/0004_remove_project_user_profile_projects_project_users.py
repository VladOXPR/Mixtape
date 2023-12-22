# Generated by Django 4.2.7 on 2023-12-21 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_project_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='user',
        ),
        migrations.AddField(
            model_name='profile',
            name='projects',
            field=models.ManyToManyField(blank=True, related_name='projects', to='core.project'),
        ),
        migrations.AddField(
            model_name='project',
            name='users',
            field=models.ManyToManyField(blank=True, related_name='users', to='core.profile'),
        ),
    ]