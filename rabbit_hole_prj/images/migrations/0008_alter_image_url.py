# Generated by Django 4.0.5 on 2022-11-14 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0007_remove_image_height_remove_image_width_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='url',
            field=models.URLField(blank=True, default='C:\\Users\\cmyer\\OneDrive\\CMC Services\\Desktop\\Projects\\sprint_to_success\\rabbit_hole_backend\\rabbit_hole_prj', verbose_name='URL'),
        ),
    ]
