from os import name
from tabnanny import verbose
from typing import Any
from django.db import models

# Create your models here.

class Categories(models.Model):
    name: Any = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug: Any = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table: str = 'category'
        verbose_name: str = 'Категорию'
        verbose_name_plural: str = 'Категории'
        