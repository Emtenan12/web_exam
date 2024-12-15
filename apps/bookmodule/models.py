from django.db import models

class Devolper(models.Model):
    name = models.CharField(max_length=100)


class Game(models.Model):
    title = models.CharField(max_length=100)
    devolper = models.ForeignKey(Devolper, on_delete=models.CASCADE)


