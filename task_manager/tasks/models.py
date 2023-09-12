from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver

from task_manager.statuses.models import Status
from task_manager.users.models import CustomUsers
from task_manager.labels.models import Label
from django.urls import reverse
# Create your models here.


class Task(models.Model):
    creator = models.ForeignKey(
        CustomUsers,
        on_delete=models.RESTRICT,
        verbose_name="Создатель",
        related_name="creator"
    )
    name = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(blank=True, verbose_name="Описание")
    status = models.ForeignKey(
        Status,
        on_delete=models.RESTRICT,
        verbose_name="Статус"
    )
    executor = models.ForeignKey(
        CustomUsers,
        blank=True,
        null=True,
        on_delete=models.RESTRICT,
        verbose_name="Исполнитель"
    )
    labels = models.ManyToManyField(Label, blank=True, verbose_name="Метка")
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
        return reverse('task_page', kwargs={'pk': self.pk})


# Создаем обработчик сигнала pre_delete для меток
@receiver(pre_delete, sender=Label)
def protect_labels_with_tasks(sender, instance, **kwargs):
    if instance.task_set.exists():
        # Если есть связанные задачи, не позволяйте удалить метку
        raise models.RestrictedError(
            "You can't delete a label with associated tasks.",
            [instance]
        )
