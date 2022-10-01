# Generated by Django 4.0 on 2022-10-01 08:16

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='news',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='news',
            name='preambule',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='Preambule'),
        ),
    ]
