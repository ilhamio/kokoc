from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class UserTeam(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название команды", unique=True)
    members = models.ManyToManyField(UserModel, verbose_name="Состав", related_name="teams")
    description = models.TextField(verbose_name="Описание команды")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Команда"
        verbose_name_plural = "Команды"


class TeamCompetition(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название турнира")
    is_active = models.BooleanField(default=True)
    description = models.TextField(verbose_name="Описание турнира")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Командный турнир"
        verbose_name_plural = "Командные турниры"


class PersonalCompetition(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название турнира")
    is_active = models.BooleanField(default=True)
    description = models.TextField(verbose_name="Описание турнира")
    participants = models.ManyToManyField(UserModel, verbose_name="Участники", related_name="personal_competitions")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Пользовательское соревнование"
        verbose_name_plural = "Пользовательские соревнования"
