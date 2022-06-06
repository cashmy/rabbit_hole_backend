# Generated by Django 4.0.5 on 2022-06-06 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
        ('projects', '0005_project_abbreviation'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='images.image'),
        ),
    ]
