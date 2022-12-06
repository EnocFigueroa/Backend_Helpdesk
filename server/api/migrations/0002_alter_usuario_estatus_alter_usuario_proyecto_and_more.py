# Generated by Django 4.1.3 on 2022-12-06 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='estatus',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.estatusentidad'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='proyecto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.proyecto'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='rol',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.rol'),
        ),
    ]