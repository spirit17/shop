# Generated by Django 4.0.2 on 2022-03-10 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_contact_alter_product_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='check',
            fields=[
                ('inputname', models.AutoField(primary_key=True, serialize=False)),
                ('inputEmail', models.CharField(max_length=50)),
                ('inputAddress', models.CharField(default='', max_length=70)),
                ('inputAddress2', models.CharField(default='', max_length=70)),
                ('inputCity', models.CharField(default='', max_length=70)),
                ('inputstate', models.CharField(default='', max_length=70)),
                ('inputZip', models.CharField(default='', max_length=70)),
                ('inputPhone', models.CharField(default='', max_length=70)),
            ],
        ),
    ]
