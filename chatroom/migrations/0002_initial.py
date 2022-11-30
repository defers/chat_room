# Generated by Django 4.1.1 on 2022-11-27 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('chatroom', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='profile',
            field=models.ForeignKey(db_column='user', null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.userprofile'),
        ),
        migrations.AddField(
            model_name='chatroom',
            name='author',
            field=models.ForeignKey(db_column='author', on_delete=django.db.models.deletion.CASCADE, to='users.userprofile'),
        ),
    ]
