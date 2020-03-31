from django.db import models

# Create your models here.


class Category(models.Model):
    Category_Id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=1000)

    def __str__(self):
        return self.Title


class Image(models.Model):
    url = models.URLField(max_length=50000, default=' ')
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)
    Image_Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Image = models.ImageField(upload_to="image", default=" ")

    def __str__(self):
        return self.Name