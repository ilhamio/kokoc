from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()

class Achievement(models.Model):
    name = models.CharField(verbose_name="Название достижения", max_length=255)
    description = models.TextField(verbose_name="Описание")
    time_limit = models.DurationField(verbose_name="Срок выполнения", help_text="Введите срок в формате дни:часы:минуты")
    target_value = models.PositiveIntegerField(verbose_name="Цель", help_text="Минимальное значение (например, минуты тренировки или километры пробега)")
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, through='UserAchievement', related_name='achievements')

    def __str__(self):
        return self.name


class UserAchievement(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Пользователь")
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE, verbose_name="Достижение")
    achieved_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата достижения")

    def __str__(self):
        return f"{self.user} - {self.achievement}"

    class Meta:
        verbose_name = "Достижение пользователя"
        verbose_name_plural = "Достижения пользователей"
