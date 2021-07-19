from datetime import date

from django.db import models
# Категории
from django.urls import reverse


class Category(models.Model):
    title = models.CharField("Категория", max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


# Авторы
class Author(models.Model):
    name = models.CharField("Имя", max_length=150)
    description = models.TextField("О себе")
    photo = models.ImageField("Фотография", upload_to="authors/")
    image = models.ImageField("Фото обложки", upload_to="authors/", null=True)
    url = models.SlugField(max_length=200, unique=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("author_detail", kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"


# Проекты
class Project(models.Model):
    objects = None
    title = models.CharField("Название", max_length=150)
    description = models.TextField("Описание")
    created_date = models.DateField("Дата создания", default=date.today)
    publicated_date = models.DateField(auto_now=True, auto_now_add=False, editable=True)
    banner = models.ImageField("Баннер проекта", upload_to="project_banners/")
    main_picture = models.ImageField("Главная картинка", upload_to="projects/")
    preview = models.ImageField("Превью", upload_to="projects_preview/", default="projects_preview/1.png")
    author = models.ManyToManyField(Author, verbose_name="Автор", related_name="project_author")
    price = models.IntegerField("Стоимость", default=0)
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=200, unique=True)
    publicate = models.BooleanField("Опубликован", default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("project_detail", kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"


# Картинки проекта
class ProjectShots(models.Model):
    title = models.CharField("Название", max_length=150)
    description = models.TextField("Описание")
    image = models.ImageField("Изображения", upload_to="project_shots/")
    project = models.ForeignKey(Project, verbose_name="Проект", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Картинка проекта"
        verbose_name_plural = "Картинки проекта"


# База номеров клиентов
class PhoneNumber(models.Model):
    date = models.DateField("Дата добавления", default=date.today)
    number = models.CharField("Номер телефона", max_length=50)

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = "Номер"
        verbose_name_plural = "Номера"

