from django.db import models


def upload_path(instance, filname):
    return '/'.join(['covers', str(instance.Nom), filname])
class User(models.Model):
    Nom = models.CharField(max_length=255)
    Prenom = models.CharField(max_length=255)
    mobile = models.IntegerField()
    picture = models.ImageField(blank=True, null=True, upload_to=upload_path)
    Email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    datedenaisance = models.DateTimeField(auto_now_add=True)
    adresse = models.CharField(max_length=255)
    description = models.TextField()
    sexe = models.CharField(max_length=255)
    statue = models.BooleanField()

    def __str__(self):
        return '%s %s %s %s %s %s %s %s %s%s %s' % (
        self.Nom, self.Prenom, self.mobile, self.picture, self.Email, self.password, self.datedenaisance, self.adresse,
        self.description, self.sexe, self.statue)




class Patient(User):
    identifiant = models.IntegerField()
    identifiantClinique=models.CharField(max_length=255)
    Groupesanguin=models.CharField(max_length=255)
    maladiechronique=models.CharField(max_length=255)

    def __str__(self):
        return ' %s %s %s %s %s %s %s %s %s%s %s %s %s %s %s' % (self.Nom, self.Prenom,self.mobile,self.picture,self.Email,self.password,self.datedenaisance,self.adresse,self.description,self.sexe,self.statue,self.identifiant,self.identifiantClinique,self.Groupesanguin,self.maladiechronique)
class Doctor(User):
    Desination= models.CharField(max_length=255)
    specialite=models.CharField(max_length=255)
    Patients=models.ManyToManyField(Patient)
    def __str__(self):
        return ' %s %s %s %s %s %s %s %s %s%s %s %s %s %s' % (self.Nom, self.Prenom,self.mobile,self.picture,self.Email,self.password,self.datedenaisance,self.adresse,self.description,self.sexe,self.statue,self.Desination,self.specialite,self.Patients)


class clinique(User):


    def __str__(self):
        return self.name
class patient_Clinique(models.Model):
    Doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, editable=True, default=None)
    Patient = models.ForeignKey(Patient, on_delete=models.CASCADE, editable=True, default=None)

    def __str__(self):
        return  str(self.pk)
