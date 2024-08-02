from django.db import models

class Projects(models.Model):
    title = models.CharField('Название', max_length=150)
    intro = models.CharField('Интро', max_length=500)
    full_text = models.TextField('Проект')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
