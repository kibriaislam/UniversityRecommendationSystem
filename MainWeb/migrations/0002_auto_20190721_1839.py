# Generated by Django 2.2.1 on 2019-07-21 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainWeb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='engineering_university',
            name='passingyear',
            field=models.IntegerField(default=2019),
        ),
        migrations.AlterField(
            model_name='general_university_requirement',
            name='passingyear',
            field=models.IntegerField(default=2019),
        ),
        migrations.AlterField(
            model_name='medical_college',
            name='passingyear',
            field=models.IntegerField(default=2019),
        ),
        migrations.AlterField(
            model_name='science_and_technology_requirement',
            name='passingyear',
            field=models.IntegerField(default=2019),
        ),
    ]
