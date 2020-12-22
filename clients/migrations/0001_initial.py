# Generated by Django 3.1.4 on 2020-12-21 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=30)),
                ('age', models.PositiveIntegerField()),
                ('salary', models.DecimalField(decimal_places=2, max_digits=12)),
                ('intro', models.TextField(blank=True, null=True)),
                ('pfp', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
