# Generated by Django 4.0.6 on 2022-07-14 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField(max_length=50)),
                ('Date_of_birth', models.DateField()),
                ('Gender', models.TextField(max_length=5)),
                ('Phone_number', models.IntegerField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address1', models.TextField(max_length=75)),
                ('address2', models.TextField(max_length=75)),
                ('pincode', models.IntegerField(max_length=5)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sitee.profile')),
            ],
        ),
    ]
