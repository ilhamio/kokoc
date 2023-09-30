from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


# Create your models here.
class Charity(models.Model):
    organization_name = models.CharField(verbose_name="Название организации", max_length=255)
    name = models.CharField(verbose_name="Название фонда", max_length=255)
    is_active = models.BooleanField(verbose_name="Активность", default=False)
    approved = models.BooleanField(verbose_name="Подтверждено администратором", default=False)
    description = models.CharField(verbose_name="Описание")
    contact_email = models.EmailField(verbose_name="Почта для связи")
    sum = models.DecimalField(verbose_name="Сумма сбора", max_digits=15, decimal_places=2)
    got_sum = models.DecimalField(verbose_name="Собранная сумма", max_digits=15, decimal_places=2)


class UserCharity(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='charities', on_delete=models.CASCADE,
                                verbose_name="Пользователь")
    charity = models.OneToOneField(Charity, related_name="users", on_delete=models.CASCADE, verbose_name="Фонд")
    sum = models.DecimalField(verbose_name="Собранная сумма", max_digits=15, decimal_places=2)
    created_at = models.DateTimeField(verbose_name="Время совершения пожертвования", auto_created=True)


class CharitySubscription(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='subscription', on_delete=models.CASCADE,
                                verbose_name="Пользователь")
    charity = models.OneToOneField(Charity, related_name="users", on_delete=models.CASCADE, verbose_name="Фонд")
    sum = models.DecimalField(verbose_name="Сумма пожертвования", max_digits=15, decimal_places=2)
    days = models.IntegerField(verbose_name="Количество дней")
    created_at = models.DateTimeField(verbose_name="Время создания подписки", auto_created=True)