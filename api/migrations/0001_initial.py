# Generated by Django 3.2.8 on 2021-10-29 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dbModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field1', models.CharField(default='', max_length=8, unique=True)),
                ('field2', models.CharField(max_length=50, unique=True)),
                ('blfield3', models.BooleanField(default=False)),
                ('intfield', models.IntegerField(default=0)),
                ('datefield', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
