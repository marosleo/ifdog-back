# Generated by Django 4.1.1 on 2022-11-30 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_usuario_foto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentarios',
            name='publicado',
        ),
    ]