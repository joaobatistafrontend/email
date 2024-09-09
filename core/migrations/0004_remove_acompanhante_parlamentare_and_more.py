# Generated by Django 4.2.16 on 2024-09-09 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rename_parlamentares_acompanhante_parlamentare'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='acompanhante',
            name='parlamentare',
        ),
        migrations.AddField(
            model_name='acompanhante',
            name='parlamentares',
            field=models.ManyToManyField(to='core.parlamentares'),
        ),
        migrations.AlterField(
            model_name='acompanhante',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
