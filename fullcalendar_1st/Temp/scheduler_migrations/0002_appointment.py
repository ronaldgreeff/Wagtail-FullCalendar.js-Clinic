# Generated by Django 2.2.9 on 2020-02-23 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myusers', '0002_doctor_patient'),
        ('scheduler', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('doctor', models.OneToOneField(on_delete='CASCADE', to='myusers.Doctor')),
                ('patient', models.OneToOneField(on_delete='CASCADE', to='myusers.Patient')),
                ('service', models.ForeignKey(null=True, on_delete='CASCADE', to='scheduler.Service')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
