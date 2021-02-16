from django.db import models


class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    subtitle = models.CharField('Подпись', max_length=100 )
    description = models.TextField('Описание')

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'



    def __str__(self):
        return self.title
