from django.db import models

from core.models import TimeStampedModel


class Board(TimeStampedModel):
    class Meta:
        verbose_name = '게시판'
        verbose_name_plural = verbose_name
        ordering = ('-created_at',)

    title = models.CharField('제목', max_length=100)
    content = models.TextField('내용', blank=True)

    def __str__(self):
        return f'<{self.id}> {self.title}'
