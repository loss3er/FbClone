# Generated by Django 4.1.7 on 2023-04-28 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='index',
            old_name='Fname',
            new_name='sF_Name',
        ),
        migrations.RenameField(
            model_name='index',
            old_name='Lname',
            new_name='sL_Name',
        ),
        migrations.RenameField(
            model_name='index',
            old_name='email',
            new_name='sM_Email',
        ),
        migrations.RenameField(
            model_name='index',
            old_name='password',
            new_name='sPass',
        ),
        migrations.RemoveField(
            model_name='index',
            name='phone',
        ),
        migrations.AddField(
            model_name='index',
            name='date',
            field=models.DateField(default=555),
            preserve_default=False,
        ),
    ]
