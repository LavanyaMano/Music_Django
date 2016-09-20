from django.db import models


class Album(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    tracks = models.ManyToManyField('Track',blank=True)
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Track(models.Model):
    name = models.CharField(max_length=100)
    artists = models.ManyToManyField('Artist',blank=True)
    genres = models.ManyToManyField('Genre',blank=True)

    class Meta:
        ordering = ['name',]

    def __str__(self):
        return self.name

class Artist(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Genre(models.Model):
    AFRICAN = 'african'
    ASIAN = 'asian'
    BLUES = 'blues'
    CARIBBEAN ='caribbean'
    COMEDY = 'comedy'
    COUNTRY = 'country'
    ELECTRONIC = 'electronic'
    FOLK = 'folk'
    HIPHOP ='hiphop'
    JAZZ = 'jazz'
    LATIN ='latin'
    POP = 'pop'
    ROCK = 'rock'
    OTHERS ='others'
    CATEGORY_CHOICES = (
        (AFRICAN, 'African'),
        (ASIAN, 'Asian'),
        (BLUES, 'Blues'),
        (CARIBBEAN,'Caribbean'),
        (COMEDY, 'Comedy'),
        (COUNTRY, 'Country'),
        (ELECTRONIC, 'Electronic'),
        (FOLK, 'Folk'),
        (HIPHOP,'Hiphop'),
        (JAZZ, 'Jazz'),
        (LATIN,'Latin'),
        (POP, 'Pop'),
        (ROCK, 'Rock'),
        (OTHERS,'Others'),
        )
    name = models.CharField(max_length=50, unique = True)
    category = models.CharField(max_length=50,
        default = OTHERS, choices= CATEGORY_CHOICES)

    def __str__(self):
        return "{}, {}".format(self.name,self.category)


        


