# Generated by Django 2.0 on 2018-01-09 21:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Doc', '0003_auto_20180109_2143'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=250)),
                ('LastName', models.CharField(max_length=250)),
                ('IdNumber', models.CharField(max_length=250)),
                ('Disease', models.CharField(max_length=250)),
                ('body', models.TextField()),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('admitted', 'Admitted'), ('outpatient', 'OutPatient')], default='draft', max_length=10)),
            ],
            options={
                'ordering': ('-publish',),
            },
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
