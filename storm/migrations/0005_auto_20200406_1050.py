# Generated by Django 2.2.6 on 2020-04-06 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storm', '0004_auto_20200405_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='idea_file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]