from django.db import models
from django.db.models import UniqueConstraint, Q


class Book(models.Model):
    name = models.CharField('book name', max_length=100, unique=True)
    author = models.ForeignKey('Autor', on_delete=models.CASCADE, related_name='books')
    publisher_data = models.DateField('date published')
    registered = models.BooleanField(null=True)
    manager = models.BooleanField(null=True)
    publisher_id = models.ForeignKey('Publisher', on_delete=models.CASCADE, related_name='books', null=True)

    class Meta:
        db_table = 'books'
        ordering = ['-publisher_data']
        get_latest_by = 'publisher_data'
        # unique_together = ('publisher_data', 'name')
        unique_together = ('publisher_data', 'name')  # Оставляем это
        # index_together = ('name', 'autor')
        indexes = [models.Index(fields=['name', 'author'])]  # Используйте indexes вместо index_together

        constraints = [UniqueConstraint(fields=['name'], condition=Q(registered=True), name='unique_title_registered')]
        verbose_name = 'fiction book'  # Человекочитаемое имя модели
        verbose_name_plural = 'fiction books'  # Человекочитаемое множественное число имени модели

    def __str__(self):
        return self.name

















#
# Создайте модель Book со следующими полями:
# Имя книги: обязательно к заполнению
# Ссылка на автора: при удалении автора книги пропасть не должны
# Дата публикации
# Свяжите новую модель книги с автором. У одного автора может быть много книг.









