from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()

class Charity(models.Model):
    organization_name = models.CharField(verbose_name="Название организации", max_length=255)
    name = models.CharField(verbose_name="Название фонда", max_length=255)
    is_active = models.BooleanField(verbose_name="Активность", default=False)
    approved = models.BooleanField(verbose_name="Подтверждено администратором", default=False)
    description = models.CharField(verbose_name="Описание", max_length=255)
    contact_email = models.EmailField(verbose_name="Почта для связи")
    sum = models.DecimalField(verbose_name="Сумма сбора", max_digits=15, decimal_places=2)
    got_sum = models.DecimalField(verbose_name="Собранная сумма", max_digits=15, decimal_places=2)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, through='UserCharity', related_name='charities')

class UserCharity(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Пользователь")
    charity = models.ForeignKey(Charity, on_delete=models.CASCADE, verbose_name="Фонд")
    sum = models.DecimalField(verbose_name="Собранная сумма", max_digits=15, decimal_places=2)
    created_at = models.DateTimeField(verbose_name="Время совершения пожертвования", auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.charity}"

    class Meta:
        verbose_name = "Связь пользователя с фондом"
        verbose_name_plural = "Связи пользователей с фондами"

class CharitySubscription(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='subscription', on_delete=models.CASCADE,
                                verbose_name="Пользователь")
    charity = models.ForeignKey(Charity, related_name="subscriptions", on_delete=models.CASCADE, verbose_name="Фонд")
    sum = models.DecimalField(verbose_name="Сумма пожертвования", max_digits=15, decimal_places=2)
    days = models.IntegerField(verbose_name="Количество дней")
    created_at = models.DateTimeField(verbose_name="Время создания подписки", auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.charity}"

    class Meta:
        verbose_name = "Связь пользователя с фондом"
        verbose_name_plural = "Связи пользователей с фондами"
