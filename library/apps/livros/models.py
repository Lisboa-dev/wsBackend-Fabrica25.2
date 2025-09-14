from django.db import models


class Books(models.Model):
    title = models.CharField(
        max_length=255,
        null=False,
        blank=False,
    )
   
    author = models.CharField(
        max_length=500,
        null=False,
        blank=False,
    )

    genres = models.CharField(
        max_length=500,
        null=False,
        blank=False,
    )

 
    url = models.URLField(
        max_length=500,
        null=True,
        blank=True,
    )
    
    image_url = models.URLField(
        null=False,
        blank=False,
        max_length=500,
        default="Indefinido",
    )

    date_publi = models.IntegerField(
        null=False,
        blank=False,
    )

    availability = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        default="Indefinido",
    )

    format = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        default="Indefinido",
    )

    number_pages = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

    publisher = models.CharField(
        max_length=500,
        null=True,
        blank=True,
    )

    languages = models.CharField(
        max_length=250,
        null=True,
        blank=True,
    )

    cluster = models.ForeignKey(
        "clusters.Clusters",  
        on_delete=models.CASCADE,
        related_name="books"  
    )

    def __str__(self):
        return f"{self.title} ({self.author})"



objects = models.Manager()


