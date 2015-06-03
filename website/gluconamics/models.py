from django.db import models


class Visiter(models.model):
    email = models.EmailField()
    date = models.DateTimeField(auto_now=True)
