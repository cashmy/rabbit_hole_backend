# Generated by Django 4.0.5 on 2022-11-22 02:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('solutions', '0002_remove_solution_rabbit_hole'),
        ('rabbit_holes', '0002_remove_rabbit_hole_solution'),
    ]

    operations = [
        migrations.AddField(
            model_name='rabbit_hole',
            name='solution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rabbit_holes', to='solutions.solution'),
        ),
    ]
