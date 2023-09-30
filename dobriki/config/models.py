from django.db import models

class Config(models.Model):
    name = models.CharField(max_length=255, verbose_name="Наименование")
    coefficient = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Коэффициент", default=0.0)
    description = models.TextField(verbose_name="Описание", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Настройка активности"
        verbose_name_plural = "Настройки активности"
