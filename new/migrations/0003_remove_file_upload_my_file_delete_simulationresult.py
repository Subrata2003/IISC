# Generated by Django 4.1.5 on 2023-03-18 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0002_simulationresult'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file_upload',
            name='my_file',
        ),
        migrations.DeleteModel(
            name='SimulationResult',
        ),
    ]