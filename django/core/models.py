from django.db import models


class TimeStampedModel(models.Model):
    class Meta:
        abstract = True
    created_at = models.DateTimeField('생성일', auto_now_add=True)
    updated_at = models.DateTimeField('수정일', auto_now=True)

    @property
    def created_date(self):
        return self.created_at.strftime('%Y-%m-%d')

    @property
    def updated_date(self):
        return self.updated_at.strftime('%Y-%m-%d')
