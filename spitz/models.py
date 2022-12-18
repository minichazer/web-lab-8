from django.db import models
from django.urls import reverse

class Spitz(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    typeS = models.ForeignKey("TypesSpitz", on_delete=models.PROTECT, null=True)
    lastedit_date = models.DateTimeField()

    def __str__(self):
        return self.title

class TypesSpitz(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    lastedit_date = models.DateTimeField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('type', kwargs={'type_id': self.pk})    

# class SiteMapModel(models.Model):
#     title = models.CharField(max_length=120)
#     url = models.CharField(max_length=140)
#     date = models.DateField()

#     def get_absolute_url(self):
#         return f'/{self.pk}'