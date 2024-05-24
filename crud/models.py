from django.db import models

# Create your models here.


class Post(models.Model):
    title= models.CharField(max_length=200)
    body= models.TextField()
    image= models.ImageField(default="null",upload_to="articles")
    author= models.ForeignKey("auth.User",on_delete=models.CASCADE,)

    def __str__(self):

        return self.title
        