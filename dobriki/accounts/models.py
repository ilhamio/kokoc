from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class UserProfile(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, verbose_name="Пользователь")
    height = models.IntegerField(verbose_name="Рост", blank=True, null=True)
    weight = models.DecimalField(verbose_name="Вес", max_digits=5, decimal_places=2, blank=True, null=True)
    age = models.IntegerField(verbose_name="Возраст", blank=True, null=True)

    def __str__(self):
        return f"Профиль пользователя {self.user.username}"

    class Meta:
        verbose_name = "Профиль пользователя"
        verbose_name_plural = "Профили пользователей"
