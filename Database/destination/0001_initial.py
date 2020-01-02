# Generated by Django 2.2.7 on 2019-12-25 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('blood_group', models.CharField(max_length=5)),
                ('address', models.CharField(max_length=100)),
                ('phone_no', models.BigIntegerField(default=0)),
            ],
        ),
    ]
