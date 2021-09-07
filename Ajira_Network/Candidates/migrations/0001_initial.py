# Generated by Django 3.2.7 on 2021-09-07 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], default='male', max_length=20)),
                ('mobile', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=30)),
                ('expected_salary', models.IntegerField()),
                ('will_relocate', models.BooleanField(default=False)),
            ],
        ),
    ]
