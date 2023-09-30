from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class UserTeam(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название команды")
    members = models.ManyToManyField(UserModel, verbose_name="Состав", related_name="teams")
    description = models.CharField(max_length=512, verbose_name="Описание команды")
