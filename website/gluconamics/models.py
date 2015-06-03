from django.db import models


class Visitor(models.Model):
    email = models.EmailField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email
