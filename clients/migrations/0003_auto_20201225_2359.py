# Generated by Django 3.1.4 on 2020-12-25 23:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_auto_20201222_0321'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='pfp',
            new_name='foto',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='age',
            new_name='idade',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='name',
            new_name='nome',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='salary',
            new_name='salário',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='surname',
            new_name='sobrenome',
        ),
    ]