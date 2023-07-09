# Créé par chari, le 19/03/2023 en Python 3.7
"""
    Ce fichier permet de creer le fond d'un niveau
    à l'aide des listes Ligne1,Ligne2...
"""

# Importation des biblio
from Constantes_Jeu import *


# Initialisation du jeu
import pygame
from random import *
from pygame.locals import *
pygame.init()

# Design de la fenêtre Pygame
fenetre = pygame.display.set_mode((longueur_fenetre , largeur_fenetre))
#  Titre
pygame.display.set_caption(titre_fenetre)

# Chargement des images pour le fond
mur = pygame.image.load(image_Mur).convert()
mur = pygame.transform.scale(mur,(taille_sprite,taille_sprite))
eau = pygame.image.load(image_Eau).convert()
eau = pygame.transform.scale(eau,(taille_sprite,taille_sprite))
herbe = pygame.image.load(image_Herbe).convert()
herbe = pygame.transform.scale(herbe,(taille_sprite,taille_sprite))
obstacle = pygame.image.load(image_Obstacle).convert()
obstacle = pygame.transform.scale(obstacle,(taille_sprite,taille_sprite))
porte = pygame.image.load(image_Door_1).convert()
porte = pygame.transform.scale(porte,(taille_sprite,taille_sprite))
porte_2 = pygame.image.load(image_Door_2).convert()
porte_2 = pygame.transform.scale(porte_2,(taille_sprite,taille_sprite))
passage = pygame.image.load(image_Passage).convert()
passage = pygame.transform.scale(passage,(taille_sprite,taille_sprite))

Ligne0 = ['m' for i in range(0,nbr_sprite_longueur)] #Que des Murs
Ligne1 = list('mHHmHHHHHHHHHmHHHHHm')
Ligne2 = list('mPHmHHmmmmmmmmHHHHHm')
Ligne3 = list('mmmmHHHHHmHHHmHHHHHm')
Ligne4 = list('mHHHHHmmHmHHHmHHHHmm')
Ligne5 = list('mmmmmHmHEHHHmHHHHHHm')
Ligne6 = list('mHHHmHHHEHmmHHHHHHHm')
Ligne7 = list('mHHHmmHHHHmHHHmmmHHm')
Ligne8 = list('mmmHmHHmmmHHHHHmHHHm')
Ligne9 = list('mHHHHHHHHHHHmmHHmmmm')
Ligne10 = list('mEEEHHHHHHmmHmmHHHHm')
Ligne11 = list('mHHHHHHHHHHHHHXmHHHm')
Ligne12 = list('mPHHmHHHmHHHHHHmHHHm')
Ligne13 = list('mHHHmHHHmHHHHHHmHHHm')
Ligne14 = ['m' for i  in range(0,nbr_sprite_longueur)] #Que des Murs

L = [Ligne0,Ligne1,Ligne2,Ligne3,Ligne4,Ligne5,Ligne6,Ligne7,Ligne8,Ligne9,Ligne10,Ligne11,Ligne12,Ligne13,Ligne14]



def fond_niveau(L):
    numero_ligne = 0
    for ligne in L :
        numero_case = 0
        # parcours de la ième ligne
        for sprite in ligne:
            x = numero_case*taille_sprite
            y = numero_ligne*taille_sprite
            if sprite == "E":
                fenetre.blit(eau,(x,y))
            elif sprite == "m":
                fenetre.blit(mur,(x,y))
            elif sprite == "P":
                fenetre.blit(passage,(x,y))
            elif sprite == "X":
                fenetre.blit(porte_2,(x,y))
            elif sprite == "S":
                fenetre.blit(eau,(x,y))
            elif sprite == "O":
                fenetre.blit(obstacle,(x,y))
            else :
                fenetre.blit(herbe,(x,y))

            numero_case += 1
        numero_ligne += 1
    pygame.image.save(fenetre,'images/niveau.bmp')

