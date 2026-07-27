from django.db import models

# Create your models here.


class Portfolio(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField()
    technologies = models.CharField(max_length=200)
    image = models.ImageField(upload_to="projets/")
    lien_github = models.URLField(blank=True)
    lien_demo = models.URLField(blank=True)

    def __str__(self):
        return self.titre