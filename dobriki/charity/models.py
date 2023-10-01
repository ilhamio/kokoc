from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Charity(models.Model):
    organization_name = models.CharField(verbose_name="Название организации", max_length=255)
    name = models.CharField(verbose_name="Название фонда", max_length=255)
    is_active = models.BooleanField(verbose_name="Активность", default=False)
    approved = models.BooleanField(verbose_name="Подтверждено администратором", default=False, editable=False)
    description = models.CharField(verbose_name="Описание", max_length=255)
    contact_email = models.EmailField(verbose_name="Почта для связи", blank=True, null=True)
    sum = models.DecimalField(verbose_name="Сумма сбора", max_digits=15, decimal_places=2)

    def __str__(self):
        return f"Фонд {self.name}"

    class Meta:
        verbose_name = "Фонд"
        verbose_name_plural = "Фонды"


class CharitySubscription(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='subscription', on_delete=models.CASCADE,
                                verbose_name="Пользователь")
    charity = models.ForeignKey(Charity, related_name="subscriptions", on_delete=models.CASCADE, verbose_name="Фонд")
    created_at = models.DateTimeField(verbose_name="Время создания подписки", auto_now_add=True, auto_created=True)

    def __str__(self):
        return f"{self.user} - {self.charity}"

    class Meta:
        verbose_name = "Подписка на пожертвования"
        verbose_name_plural = "Подписка на пожертвования"


class Wallet(models.Model):
    user = models.OneToOneField(UserModel, related_name='wallet', on_delete=models.CASCADE, verbose_name="Пользователь")
    balance = models.DecimalField(max_digits=18, decimal_places=2, verbose_name="Баланс", default=0)

    def __str__(self):
        return f"Кошелек {self.user}"

    class Meta:
        verbose_name = "Кошелек"
        verbose_name_plural = "Кошельки"


class Transaction(models.Model):
    user = models.ForeignKey(UserModel, related_name='tra', on_delete=models.CASCADE, verbose_name="Пользователь")
    sum = models.DecimalField(max_digits=18, decimal_places=2, verbose_name="Cумма перевода")
    fund = models.OneToOneField(Charity, related_name='transactions', on_delete=models.CASCADE, verbose_name="Фонд")
    created_at = models.DateTimeField(auto_created=True, auto_now=True, verbose_name="Дата проведения транзакции")

    def __str__(self):
        return f"Транзакция {self.user} в фонд {self.fund}"

    class Meta:
        verbose_name = "Транзакция"
        verbose_name_plural = "Транзакции"
