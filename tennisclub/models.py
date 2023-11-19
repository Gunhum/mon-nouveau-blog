from django.db import models


class Equipement(models.Model):
    id_equip = models.CharField(max_length=100, primary_key=True)
    disponibilite = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='static/image/')
    capa = models.IntegerField()
    place = models.IntegerField()

    def __str__(self):
        return self.id_equip


class Character(models.Model):
    id_character = models.CharField(max_length=100, primary_key=True)
    etat = models.CharField(max_length=20)
    nom= models.CharField(max_length=20)
    prenom = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='static/image/')
    lieu = models.ForeignKey(Equipement, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_character

#a faire a chaque modif:
#python manage.py makemigrations tennisclub
#python manage.py migrate tennisclub
