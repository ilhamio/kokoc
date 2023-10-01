from django.utils.translation import gettext_lazy as _

from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class Activity(models.Model):
    class NameChoice(models.TextChoices):
        STEPS = "STEP", _("Steps")
        SKI = "SKI", _("Ski")
        RUN = "RUNNING", _("Running")
        BYCYCLE = "BYCYCLE", _("Bycycle")
        FOUND_DOBRIK = "FOUND", _("Found dobrik")

    name = models.CharField(max_length=255, verbose_name="Наименование")
    type = models.CharField(max_length=32, choices=NameChoice.choices)
    coeff = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Коэффициент")
    description = models.TextField(verbose_name="Описание", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Настройка активности"
        verbose_name_plural = "Настройки активности"


class ActivityConverter(models.Model):
    step_count = models.PositiveIntegerField(verbose_name="Количество шагов", default=0)
    distance = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Расстояние")
    time = models.IntegerField(verbose_name="Время")
    kcal = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Калории")
    activity = models.OneToOneField(Activity, on_delete=models.CASCADE, verbose_name="Активность")

    def __str__(self):
        return f"Коэффициенты {self.pk}"

    class Meta:
        verbose_name = "Настройка коэффициентов"
        verbose_name_plural = "Настройки коэффициентов"


class ActivityIndicators(models.Model):
    step_count = models.PositiveIntegerField(verbose_name="Количество шагов", default=0)
    distance = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Расстояние")
    time = models.IntegerField(verbose_name="Время")
    kcal = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Калории")
    activity_type = models.ForeignKey(Activity, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Aim(models.Model):
    user = models.ForeignKey(to=UserModel, verbose_name="Пользователь", related_name='aim',on_delete=models.CASCADE)
    step_aim = models.PositiveBigIntegerField(verbose_name="Цель по шагам", default=10000)

    def __str__(self):
        return f"Цель по шагам для {self.user}"

    class Meta:
        verbose_name = "Цель"
        verbose_name_plural = "Цели"


class ActivitySnapshot(ActivityIndicators, models.Model):
    user = models.ForeignKey(to=UserModel, verbose_name="Пользователь", on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(verbose_name="Дата и время создания", auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"Слепок прогресса для {self.user}"
