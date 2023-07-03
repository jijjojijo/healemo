from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from coach.models import Coach


class Quiz(models.Model):
    """Quiz model"""
    title = models.CharField(_('title'), max_length=255)
    description = models.TextField(_('description'))
    image = models.ImageField(_('image'), upload_to='quiz/')
    category = models.ForeignKey('Category', on_delete=models.SET_NULL,
                                 null=True, related_name='category', verbose_name=_('category'))
    draft = models.BooleanField(_('draft'), default=False)
    slug = models.SlugField(_('slug'), max_length=255, unique=True)

    class Meta:
        indexes = [
            models.Index(fields=['slug'])
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("quiz_detail", kwargs={"slug": self.slug})


class Rank(models.Model):
    """Quiz Rang model"""
    description = models.TextField(_('description'))
    min_power = models.PositiveSmallIntegerField(_('min power'), default=0)
    max_power = models.PositiveSmallIntegerField(_('max power'), default=0)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='results', verbose_name=_('quiz'))
    coach = models.ForeignKey(Coach, related_name='coaches', verbose_name=_('coaches'), blank=True, null=True,
                              on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.pk}: {self.min_power} - {self.max_power}'


class Category(models.Model):
    """Quiz Category"""
    title = models.CharField(_('name'), max_length=255)
    slug = models.SlugField(_('slug'), max_length=255)

    def __str__(self):
        return self.title


class Question(models.Model):
    """Quiz Question"""
    title = models.CharField(_('title'), max_length=255)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions', verbose_name=_('quiz'))

    def __str__(self):
        return self.title


class Option(models.Model):
    """The answer to the question"""
    title = models.CharField(_('title'), max_length=255)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers', verbose_name=_('question'))
    power = models.PositiveSmallIntegerField(_('power'), default=0)

    def __str__(self):
        return self.title


class Result(models.Model):
    """Результат тестов"""
    code = models.CharField(_('code'), max_length=10, unique=True)
    quiz_id = models.PositiveSmallIntegerField(_('quiz id'))
    value = models.PositiveSmallIntegerField(_('value'))

    def __str__(self):
        return self.code

    class Meta:
        indexes = [
            models.Index(fields=['code'])
        ]

    def get_absolute_url(self):
        return reverse("result", kwargs={"code": self.code})
