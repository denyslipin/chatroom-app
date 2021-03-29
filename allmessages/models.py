from django.db import models


class AllMessages(models.Model):
    email = models.EmailField(max_length=25)
    message = models.CharField(max_length=100)
    create_date = models.DateTimeField('date created')
    update_date = models.DateTimeField('date updated')
