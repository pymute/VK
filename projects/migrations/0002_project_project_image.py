# Generated by Django 4.2.5 on 2023-10-04 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_image',
            field=models.ImageField(blank=True, default='testlogo.png', null=True, upload_to=''),
        ),
    ]