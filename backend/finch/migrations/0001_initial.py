# Generated by Django 3.2.9 on 2023-09-03 17:03

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SandboxAccess',
            fields=[
                ('record_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('access_token', models.CharField(max_length=200)),
                ('provider_name', models.CharField(max_length=25)),
                ('company_id', models.CharField(max_length=50)),
                ('created_time', models.BigIntegerField()),
                ('latest_bool', models.BooleanField(default=True)),
            ],
        ),
    ]
