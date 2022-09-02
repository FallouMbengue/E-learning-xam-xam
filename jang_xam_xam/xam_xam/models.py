from tkinter import CASCADE
from django.db import models

# Create your models here.

class User(models.Model):
    id_user= models.AutoField(primary_key=True)
    nom= models.CharField(max_length=40)
    prenom= models.CharField(max_length=100)
    birthday=models.DateField()
    placeborn= models.CharField()
    Email= models.EmailField()
    Telephone=models.CharField( max_length=50)
    Photo_Profile=models.ImageField()

class Admin(User):
    id_admin=models.AutoField(primary_key=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

class Module(models.Model):
    id_module=models.AutoField(primary_key=True)
    intitulé=models.CharField(max_length=255)
    description=models.TextField()
    prerequis=models.TextField()
    condition=models.TextField()
    auteurs=models.TextField()
    date_de_publication=models.DateField()

class Tableau_de_bord(models.Model):
    date__debut=models.DateField()
    duree_deja_fait=models.TimeField()
    chapitres_deja_appris=models.CharField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    module=models.ForeignKey(Module,on_delete=models.CASCADE)

class Categorie(models.Model):
    id_categorie=models.AutoField()
    intitulé=models.CharField(max_length=255)
    module=models.ForeignKey(Module,on_delete=models.CASCADE)

class Chapitre(Module):
    id_chapitre=models.AutoField(primary_key=True)
    intitulé=models.CharField(max_length=255)
    status=models.CharField(max_length=255)

class quizz(models.Model):
    id_quizz=models.AutoField(primary_key=True)
    question=models.TextField()
    reponse=models.TextField()
    status=models.CharField(max_length=255)
    chapitre=models.ForeignKey(Chapitre,on_delete=models.CASCADE)

class certification(quizz):
    date_de_certification=models.DateField()
    module=models.ForeignKey(Module, on_delete=models.CASCADE)

class Sous_chapitre(Chapitre):
    intitulé=models.CharField(max_length=255)
    Texte=models.TextField()
    vidéo=models.CharField(max_length=255)
    vidéo_demonstration=models.CharField(max_length=255)