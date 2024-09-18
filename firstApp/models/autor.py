from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# models/autor.py
class Autor(models.Model):
    name = models.CharField(max_length=100, verbose_name="Autor first name")
    last_name = models.CharField(max_length=100, verbose_name="Autor last name")
    birst_day = models.DateField('birst day')
    profile = models.URLField('fild profile url', null=True, blank=True, help_text='URLField')
    deleted = models.BooleanField(default=False, verbose_name="Удален", help_text="when false, autor inactive")
    rating = models.FloatField(null=True, validators=[MinValueValidator(1), MaxValueValidator(10)])

    def __str__(self):
        return f"{self.name} {self.last_name}"


# Обновите уже существующую модель Author дополнительными полями:
# Профиль: ссылка на личную страницу автора, может быть не указана
# Удалён: поле, которое позволит смотреть удалён ли этот автор из базы всех авторов.
# По умолчанию все авторы активны
# Рейтинг: позволит отсматривать рейтинг популярности авторов, от 1 до 10


class Publisher(models.Model):
    name = models.CharField(max_length=75)
    register_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name









