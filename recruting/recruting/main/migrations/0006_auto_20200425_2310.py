# Generated by Django 2.2.9 on 2020-04-25 17:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import recruting.main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200422_2029'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='admin',
            managers=[
                ('objects', recruting.main.models.MyUserManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='employee',
            managers=[
                ('objects', recruting.main.models.MyUserManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='manager',
            managers=[
                ('objects', recruting.main.models.MyUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]