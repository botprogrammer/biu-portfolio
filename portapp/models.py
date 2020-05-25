from django.db import models

class ProjectModel(models.Model):
    Title = models.CharField(max_length=30)
    small_description = models.CharField(max_length=70)
    detailed_description = models.CharField(max_length=500)
    code_link = models.URLField()
    picture1 = models.ImageField()
    picture2 = models.ImageField()
    picture3 = models.ImageField()

    def __str__(self):
        return self.Title


