# Generated by Django 4.1.5 on 2023-01-02 18:54

from django.db import migrations, models
import users.manager


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_remove_user_name"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={},
        ),
        migrations.AlterModelManagers(
            name="user",
            managers=[
                ("objects", users.manager.UserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name="user",
            name="date_joined",
        ),
        migrations.RemoveField(
            model_name="user",
            name="first_name",
        ),
        migrations.RemoveField(
            model_name="user",
            name="is_active",
        ),
        migrations.RemoveField(
            model_name="user",
            name="is_staff",
        ),
        migrations.RemoveField(
            model_name="user",
            name="last_name",
        ),
        migrations.RemoveField(
            model_name="user",
            name="username",
        ),
        migrations.AddField(
            model_name="user",
            name="name",
            field=models.CharField(default=None, max_length=127),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(max_length=255, unique=True),
        ),
    ]