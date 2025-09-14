from django.db import models
from django.conf import settings


class Clusters(models.Model):

   
   name= models.CharField(
      max_length= 200,
      null=False,
      blank=False,
   )
   genres= models.CharField(
      max_length=50,
      null= False,
      blank=False
   )
   description=models.TextField(
      max_length= 1000,
      null=False,
      blank=False
   )
  

   user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="cluster"
    )
   
   def  __str__(self):
      return f"{self.titulo}{self.autor}{self.data} \n\n {self.content}\n\n {self.url}\n{self.urlToImage}"


objetos = models.Manager()

