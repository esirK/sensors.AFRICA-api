# Generated by Django 3.0.4 on 2020-03-23 11:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


def forwards_func(apps, schema_editor):
    City = apps.get_model("sensorsafrica", "City")
    City.objects.bulk_create(
        [
            City(
                city_slug="lagos",
                city_name="Lagos",
                country_code="NG"
            ),
            City(
                city_slug="nairobi",
                city_name="Nairobi",
                country_code="KE"
            ),
            City(
                city_slug="dar-es-salaam",
                city_name="Dar es Salaam",
                country_code="TZ"
            ),
        ]
    )


def reverse_func(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('city_slug', models.CharField(db_index=True, max_length=255)),
                ('city_name', models.CharField(db_index=True, max_length=255)),
                ('country_code', models.CharField(db_index=True, max_length=3)),
            ],
            options={
                'verbose_name_plural': 'Cities',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('latitude', models.DecimalField(blank=True, decimal_places=11, max_digits=14, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=11, max_digits=14, null=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sensorsafrica.City')),
            ],
            options={
                'verbose_name_plural': 'Locations',
            },
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('node_uid', models.CharField(db_index=True, max_length=255)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sensorsafrica.Location')),
                ('node_owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('sensor_uid', models.CharField(db_index=True, max_length=255)),
                ('sensor_name', models.CharField(db_index=True, max_length=255)),
                ('sensor_manufacturer', models.CharField(db_index=True, max_length=255)),
                ('node', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sensorsafrica.Node')),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
    ]