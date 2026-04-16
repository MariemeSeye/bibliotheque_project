from django.db import models


class Auteur(models.Model):
    nom = models.CharField(max_length=200)

    def __str__(self):
        return self.nom


class Etiquette(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom


class Livre(models.Model):
    titre = models.CharField(max_length=200)
    auteur = models.ForeignKey(Auteur, on_delete=models.CASCADE)
    etiquettes = models.ManyToManyField(Etiquette, blank=True)
    annee_publication = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.titre


class Emprunt(models.Model):
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE)
    date_emprunt = models.DateField(auto_now_add=True)
    date_retour = models.DateField(null=True, blank=True)
    rendu = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.livre.titre}"