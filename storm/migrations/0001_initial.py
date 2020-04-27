# Generated by Django 3.0.4 on 2020-03-30 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idea_creator_name', models.CharField(blank=True, max_length=200, null=True)),
                ('idea_creator_mail', models.EmailField(default=None, max_length=254)),
                ('idea_creation_date', models.DateTimeField(auto_now_add=True)),
                ('idea_title', models.CharField(max_length=200)),
                ('idea_description', models.TextField(blank=True, default=None, null=True)),
                ('idea_duration', models.CharField(max_length=200)),
                ('idea_file', models.FileField(blank=True, upload_to='')),
                ('idea_status', models.CharField(choices=[('Pending', 'Pending'), ('WIP', 'WIP'), ('Accepted', 'Accepted'), ('Completed', 'Completed')], max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Judge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judge_name', models.CharField(max_length=200)),
                ('judge_mail', models.EmailField(default=None, max_length=254)),
            ],
        ),
    ]