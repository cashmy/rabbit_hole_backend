# Generated by Django 4.0.5 on 2022-11-14 00:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0005_alter_image_file_name'),
        ('projects', '0004_alter_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='images.image'),
        ),
        migrations.AlterField(
            model_name='project',
            name='text_color',
            field=models.CharField(blank=True, default='#000000', max_length=50, verbose_name='text color'),
        ),
        migrations.AlterField(
            model_name='project',
            name='theme_color',
            field=models.CharField(blank=True, default='#00a2ed', max_length=50, verbose_name='theme color'),
        ),
    ]
