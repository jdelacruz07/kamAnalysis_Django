from django.db import models


class Gap(models.Model):
    is_close = models.CharField(max_length=200)
    date_selected = models.DateTimeField('date selected')

    def __str__(self):
        return self.is_close + ' ' + str(self.date_selected)
