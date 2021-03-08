from django.db import models

class User(models.Model):
    Nom = models.CharField(max_length=255)
    Prenom = models.CharField(max_length=255)
    mobile = models.IntegerField()
    picture = models.CharField(max_length=255)
    Email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    datedenaisance = models.DateTimeField(auto_now_add=True)
    adresse = models.CharField(max_length=255)
    description = models.TextField()
    sexe = models.CharField(max_length=255)
    statue = models.BooleanField()

    def __str__(self):
        return self.name


class Doctor(User):
    Desination= models.CharField(max_length=255)
    specialite=models.CharField(max_length=255)
    def __str__(self):
        return self.name



class Patient(User):
    identifiant = models.IntegerField()
    identifiantClinique=models.CharField(max_length=255)
    Groupesanguin=models.CharField(max_length=255)
    maladiechronique=models.CharField(max_length=255)

    def __str__(self):
        return self.name
class clinique(User):


    def __str__(self):
        return self.name