# Generated by Django 4.2.5 on 2023-10-01 02:15

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
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование')),
                ('type', models.CharField(choices=[('STEP', 'Steps'), ('SKI', 'Ski'), ('RUNNING', 'Running'), ('BYCYCLE', 'Bycycle'), ('FOUND', 'Found dobrik')], max_length=32)),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Настройка активности',
                'verbose_name_plural': 'Настройки активности',
            },
        ),
        migrations.CreateModel(
            name='ActivityConverter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step_count', models.PositiveIntegerField(default=0, verbose_name='Количество шагов')),
                ('distance', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Расстояние')),
                ('time', models.IntegerField(verbose_name='Время')),
                ('kcal', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Калории')),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Aim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step_aim', models.PositiveBigIntegerField(default=10000, verbose_name='Цель по шагам')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
        migrations.CreateModel(
            name='ActivitySnapshot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step_count', models.PositiveIntegerField(default=0, verbose_name='Количество шагов')),
                ('distance', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Расстояние')),
                ('time', models.IntegerField(verbose_name='Время')),
                ('kcal', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Калории')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата и время создания')),
                ('activity_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activity.activity')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
