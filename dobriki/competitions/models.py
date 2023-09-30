from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class UserTeam(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название команды", unique=True)
    members = models.ManyToManyField(UserModel, verbose_name="Состав", related_name="teams")
    description = models.TextField(verbose_name="Описание команды")


class TeamCompetition(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название турнира")
    is_active = models.BooleanField(default=True)
    description = models.TextField(verbose_name="Описание турнира")
