# Generated by Django 3.1.2 on 2022-10-18 05:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TODO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('C', 'COMPLETED'), ('F', 'PENDING')], max_length=2)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('priority', models.CharField(choices=[('1', 'COMPLETED'), ('2', 'COMPLETED'), ('3', 'COMPLETED'), ('4', 'COMPLETED'), ('5', 'COMPLETED'), ('6', 'COMPLETED'), ('7', 'COMPLETED'), ('8', 'COMPLETED'), ('9', 'COMPLETED'), ('10', 'COMPLETED')], max_length=2)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
