from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


# Create your models here.
# class Charity(models.Model):
#     organization_name = models.CharField(verbose_name="Название организации", max_length=255)
#     is_active = models.BooleanField(verbose_name="Активность", default=True)
#     description = models.CharField(verbose_name="Описание")
#
#
# class CharityFund(models.Model):
#     name = models.CharField(verbose_name="Название фонда", max_length=255)
#     is_active = models.BooleanField(verbose_name="Активность", default=True)
#     sum = models.DecimalField(verbose_name="Сумма сбора", max_digits=15, decimal_places=2)
#     got_sum = models.DecimalField(verbose_name="Собранная сумма", max_digits=15, decimal_places=2)

#
# class UserCharity(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='charities', on_delete=models.CASCADE,
#                              verbose_name="Пользователь")
#     sum = models.
