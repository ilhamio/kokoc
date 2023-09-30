from django.db import migrations, models


def create_initial_config(apps, schema_editor):
    Config = apps.get_model('config', 'Config')
    categories = [
        {"name": "Бег", "value": "1.0", "description": "Категория для бега"},
        {"name": "Ходьба", "value": "1.0", "description": "Категория для ходьбы"},
        {"name": "Лыжи", "value": "0.9", "description": "Категория для лыж"},
        {"name": "Велосипед", "value": "0.7", "description": "Категория для велосипеда"},
        {"name": "Коньки", "value": "0.9", "description": "Категория для коньков"},
        {"name": "Ролики", "value": "0.9", "description": "Категория для роликов"},
        {"name": "Добрики", "value": "0.8", "description": "Категория для добриков"},
    ]

    for category_data in categories:
        Config.objects.create(**category_data)


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Config",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="Наименование")),
                (
                    "coefficient",
                    models.DecimalField(
                        decimal_places=2,
                        default=0.0,
                        max_digits=5,
                        verbose_name="Коэффициент",
                    ),
                ),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="Описание"),
                ),
            ],
            options={
                "verbose_name": "Настройка активности",
                "verbose_name_plural": "Настройки активности",
            },
        ),
    ]
