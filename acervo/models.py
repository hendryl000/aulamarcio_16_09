from django.db import models


class Livro(models.Model):
    
    TIPO_ACERVO_CHOICES = [
        ("DIGITAL", "Digital"),
        ("FISICO", "Físico"),
    ]

    
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    ano = models.IntegerField()
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo
