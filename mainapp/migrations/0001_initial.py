# Generated by Django 2.1.12 on 2019-09-25 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Multiple',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('From', models.CharField(max_length=255)),
                ('To', models.CharField(max_length=255)),
                ('typeofdel', models.CharField(choices=[('paper', 'paper'), ('parcel', 'parcel')], max_length=255)),
                ('Dropoffto', models.CharField(choices=[('watchman', 'watchman'), ('Padosi', 'Padosi'), ('mailbox', 'mailbox')], max_length=255)),
                ('pin_no', models.IntegerField(max_length=255)),
                ('Full_name', models.CharField(max_length=255)),
                ('mobile_number', models.CharField(max_length=255)),
                ('Flat_number_and_building_name', models.CharField(max_length=255)),
                ('Area', models.CharField(max_length=255)),
                ('Land_mark', models.CharField(max_length=255)),
                ('weightrate', models.CharField(choices=[('10', '10'), ('20', '20')], max_length=255)),
                ('Describe_del', models.CharField(max_length=255)),
                ('City', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Postal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('From', models.CharField(max_length=255)),
                ('To', models.CharField(max_length=255)),
                ('typeofdel', models.CharField(choices=[('paper', 'paper'), ('parcel', 'parcel')], max_length=255)),
                ('del_pin_no', models.IntegerField(max_length=255)),
                ('Full_name', models.CharField(max_length=255)),
                ('mobile_number', models.CharField(max_length=255)),
                ('Flat_number_and_building_name', models.CharField(max_length=255)),
                ('Area', models.CharField(max_length=255)),
                ('Land_mark', models.CharField(max_length=255)),
                ('Postal_rate', models.CharField(choices=[('10', '10'), ('20', '20')], max_length=255)),
                ('weightrate', models.CharField(choices=[('10', '10'), ('20', '20')], max_length=255)),
                ('Describe_del', models.CharField(max_length=255)),
                ('City', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Single',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('From', models.CharField(max_length=255)),
                ('To', models.CharField(max_length=255)),
                ('typeofdel', models.CharField(choices=[('paper', 'paper'), ('parcel', 'parcel')], max_length=255)),
                ('Dropoffto', models.CharField(choices=[('watchman', 'watchman'), ('Padosi', 'Padosi'), ('mailbox', 'mailbox')], max_length=255)),
                ('pin_no', models.IntegerField(max_length=255)),
                ('Full_name', models.CharField(max_length=255)),
                ('mobile_number', models.CharField(max_length=255)),
                ('Flat_number_and_building_name', models.CharField(max_length=255)),
                ('Area', models.CharField(max_length=255)),
                ('Land_mark', models.CharField(max_length=255)),
                ('weightrate', models.CharField(choices=[('10', '10'), ('20', '20')], max_length=255)),
                ('Describe_del', models.CharField(max_length=255)),
                ('City', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
