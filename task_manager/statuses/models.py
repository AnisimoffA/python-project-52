from django.db import models
from django.urls import reverse_lazy


class Status(models.Model):
    name = models.CharField(
        max_length=100,
        db_index=True,
        verbose_name="Статус"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Время создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Время изменения"
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('statuses_list')

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'
        ordering = ['id']
