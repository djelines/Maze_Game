# Créé par chari, le 19/03/2023 en Python 3.7
# Importation des biblio
from Constantes_Jeu import *
from Création_Fond import *
import pygame
from random import *
from pygame.locals import *

# Initialisation du jeu
pygame.init()


#--------------------------------------------------------------#
#                        DESIGN DU JEU                         #
#--------------------------------------------------------------#

# Fond du jeu
fond_niveau(L)
image_niveau = 'images/niveau.bmp' #Importer le fond
fond_niveau = pygame.image.load(image_niveau).convert_alpha()
fenetre.blit(fond_niveau,(0,0))
pygame.display.flip()

# Musique du Jeu
pygame.mixer.music.load(audio_music)
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)

#Chargement de l'Image du héros en fonction des constances
heros = pygame.image.load(image_Knight) #Importer le sprite
heros = pygame.transform.scale(heros,(taille_sprite,taille_sprite)) #Dimension du sprite
pygame.display.flip() # Actualisation
# Deplacement du héros
position_heros = heros.get_rect()
position_heros = position_heros.move(taille_sprite*6,taille_sprite*13) # Coordonnée d'initialisation du sprite
fenetre.blit(heros,position_heros)

#Chargement de l'Image de Spike en fonction des constances
spike = pygame.image.load(image_Spike)
spike = pygame.transform.scale(spike,(taille_sprite,taille_sprite))

#Chargement de l'Image de la potion en fonction des constances
potion = pygame.image.load(image_Potion)
potion = pygame.transform.scale(potion,(taille_sprite,taille_sprite))

#Chargement de l'Image de la clé 1 en fonction des constances
key_1 = pygame.image.load(image_Key_1)
key_1 = pygame.transform.scale(key_1,(taille_sprite,taille_sprite))

#Chargement de l'Image de clé 2 en fonction des constances
key_2 = pygame.image.load(image_Key_2)
key_2 = pygame.transform.scale(key_2,(taille_sprite,taille_sprite))

#Chargement de l'Image du coeur fonction des constances
heart = pygame.image.load(image_Heart)
heart = pygame.transform.scale(heart,(taille_sprite,taille_sprite))

#Chargement de l'Image de l'épée fonction des constances
weapon = pygame.image.load(image_Weapon)
weapon = pygame.transform.scale(weapon,(taille_sprite,taille_sprite))

#Chargement de l'Image de l'arme fonction des constances
weapon2 = pygame.image.load(image_Weapon2)
weapon2 = pygame.transform.scale(weapon2,(taille_sprite,taille_sprite))

#Chargement de l'Image de la diamant fonction des constances
diamond_1 = pygame.image.load(image_Diamond_1)
diamond_1 = pygame.transform.scale(diamond_1,(taille_sprite,taille_sprite))

#Chargement de l'Image de la diamant fonction des constances
diamond_2 = pygame.image.load(image_Diamond_2)
diamond_2 = pygame.transform.scale(diamond_2,(taille_sprite,taille_sprite))

#Chargement de l'Image de la diamant fonction des constances
diamond_3 = pygame.image.load(image_Diamond_3)
diamond_3 = pygame.transform.scale(diamond_3,(taille_sprite,taille_sprite))

#Chargement de l'Image du Goblin en fonction des constances
goblin = pygame.image.load(image_Goblin)
goblin = pygame.transform.scale(goblin,(taille_sprite,taille_sprite))

#Chargement de l'Image du Goliath en fonction des constances
goliath = pygame.image.load(image_Goliath)
goliath = pygame.transform.scale(goliath,(taille_sprite,taille_sprite))

#Chargement de l'Image du Boss en fonction des constances
boss = pygame.image.load(image_Boss)
boss = pygame.transform.scale(boss,(taille_sprite,taille_sprite))
pygame.display.flip()

#Chargement de l'Image du obstacle en fonction des constances
obstacle = pygame.image.load(image_Obstacle)
obstacle = pygame.transform.scale(obstacle,(taille_sprite,taille_sprite))

#Chargement de l'Image du porte en fonction des constances
porte = pygame.image.load(image_Door_1)
porte = pygame.transform.scale(porte,(taille_sprite,taille_sprite))

#Chargement de l'Image du porte en fonction des constances
porte_2 = pygame.image.load(image_Door_2)
porte_2 = pygame.transform.scale(porte,(taille_sprite,taille_sprite))

#--------------------------------------------------------------#
#                         FONCTION DU JEU                      #
#--------------------------------------------------------------#

def affiche_matrice(L):
    for i in range(0,len(L)):
        print("ligne",i, '->', end='\t' )
        for j in range(0,len(L[0])):
            print(L[i][j], end='\t')
        print()

affiche_matrice(L)

def affiche_objets_init(L):
    #On colle l'image des items au bon endroit dans le jeu
    fenetre.blit(spike,(taille_sprite*4,taille_sprite*4)) #4 = colonne 5 = ligne
    fenetre.blit(potion,(taille_sprite*17,taille_sprite*12))
    fenetre.blit(key_1,(taille_sprite*7,taille_sprite*3))
    fenetre.blit(key_2,(taille_sprite*16,taille_sprite*8))
    fenetre.blit(heart,(taille_sprite*3,taille_sprite*6))
    fenetre.blit(weapon,(taille_sprite*2,taille_sprite*2))
    fenetre.blit(weapon2,(taille_sprite*12,taille_sprite*10))
    fenetre.blit(diamond_1,(taille_sprite*1,taille_sprite*6))
    fenetre.blit(diamond_2,(taille_sprite*12,taille_sprite*1))
    fenetre.blit(diamond_3,(taille_sprite*14,taille_sprite*1))
    fenetre.blit(goblin,(taille_sprite*11,taille_sprite*4))
    fenetre.blit(goliath,(taille_sprite*11,taille_sprite*12))
    fenetre.blit(boss,(taille_sprite*15,taille_sprite*2))
    fenetre.blit(obstacle,(taille_sprite*14,taille_sprite*4))
    fenetre.blit(obstacle,(taille_sprite*15,taille_sprite*4))
    fenetre.blit(obstacle,(taille_sprite*16,taille_sprite*4))
    fenetre.blit(obstacle,(taille_sprite*17,taille_sprite*4))
    fenetre.blit(porte,(taille_sprite*14,taille_sprite*11))
    # On place dans le chateau dans la liste L grace à F,P ou C
    L[4][4] = 'Spike'
    L[12][17] = 'Potion'
    L[3][7] = "Key_1"
    L[8][16] = "Key_2"
    L[6][3] = 'Heart'
    L[2][2] = 'Weapon'
    L[10][12] = "Weapon2"
    L[6][1] = "Diamond_1"
    L[1][12] = "Diamond_2"
    L[1][14] = "Diamond_3"
    L[4][11] = "Goblin"
    L[12][11] = "Goliath"
    L[2][15] = "Boss"
    L[4][14] = "obstacle"
    L[4][15] = "obstacle"
    L[4][16] = "obstacle"
    L[4][17] = "obstacle"
    L[11][14] = "porte"

def affiche_objets(liste_objets):
    if "Spike" in liste_objets:
        fenetre.blit(spike,(taille_sprite*4,taille_sprite*4)) #4 = colonne 5 = ligne
    if "Potion" in liste_objets:
        fenetre.blit(potion,(taille_sprite*17,taille_sprite*12))
    if "Key_1" in liste_objets:
        fenetre.blit(key_1,(taille_sprite*7,taille_sprite*3))
    if "Key_2" in liste_objets:
        fenetre.blit(key_2,(taille_sprite*16,taille_sprite*8))
    if "Heart" in liste_objets:
        fenetre.blit(heart,(taille_sprite*3,taille_sprite*6))
    if "Weapon" in liste_objets:
        fenetre.blit(weapon,(taille_sprite*2,taille_sprite*2))
    if "Weapon2" in liste_objets:
        fenetre.blit(weapon2,(taille_sprite*12,taille_sprite*10))
    if "Diamond_1" in liste_objets:
        fenetre.blit(diamond_1,(taille_sprite*1,taille_sprite*6))
    if "Diamond_2" in liste_objets:
        fenetre.blit(diamond_2,(taille_sprite*12,taille_sprite*1))
    if "Diamond_3" in liste_objets:
        fenetre.blit(diamond_3,(taille_sprite*14,taille_sprite*1))
    if "Goblin" in liste_objets:
        fenetre.blit(goblin,(taille_sprite*11,taille_sprite*4))
    if "Goliath" in liste_objets:
        fenetre.blit(goliath,(taille_sprite*11,taille_sprite*12))
    if "Boss" in liste_objets:
        fenetre.blit(boss,(taille_sprite*15,taille_sprite*2))
    if "obstacle" in liste_objets:
        fenetre.blit(obstacle,(taille_sprite*14,taille_sprite*4))
        fenetre.blit(obstacle,(taille_sprite*15,taille_sprite*4))
        fenetre.blit(obstacle,(taille_sprite*16,taille_sprite*4))
        fenetre.blit(obstacle,(taille_sprite*17,taille_sprite*4))
    if "porte" in liste_objets:
        fenetre.blit(porte,(taille_sprite*14,taille_sprite*11))

def ramassage_items(ligne,colonne):
    quete = ["Key_1","Key_2","Diamond_1","Diamond_2","Diamond_3"]
    if L[ligne][colonne] in quete:
        liste_objets.remove(L[ligne][colonne])
        L[ligne][colonne]="H"
        return True

def ramassage_vie(ligne,colonne):
    if L[ligne][colonne] == "Heart":
        liste_objets.remove("Heart")
        L[ligne][colonne]="H"
        return True

def ramassage_weapon(ligne,colonne):
    if L[ligne][colonne] == "Weapon":
        liste_objets.remove("Weapon")
        L[ligne][colonne]="H"
        return True

def ramassage_weapon_2(ligne,colonne):
    if L[ligne][colonne] == "Weapon2":
        liste_objets.remove("Weapon2")
        L[ligne][colonne]="H"
        return True

def ramassage_potion(ligne,colonne):
    if L[ligne][colonne] == "Potion":
        liste_objets.remove("Potion")
        L[ligne][colonne]="H"
        return True

def touche_boss(ligne,colonne):
    if L[ligne][colonne] == "Boss":
        liste_objets.remove("Boss")
        L[ligne][colonne]="H"
        Arme_Boss = False
        return True

def touche_ennemis(ligne,colonne):
    mechant = ["Spike","Goblin","Goliath"]
    if L[ligne][colonne] in mechant:
        liste_objets.remove(L[ligne][colonne])
        L[ligne][colonne]="H"
        Epee = False
        return True

def passage_secret(ligne,colonne):
    if  ligne == 12 and colonne == 1:
        return True

def passage_secret_2(ligne,colonne):
    if  ligne == 2 and colonne == 1:
        return True

def fin_jeu(ligne,colonne):
    if  ligne == 11 and colonne == 14:
        return True

#--------------------------------------------------------------#
#                         BOUCLE DE JEU                        #
#--------------------------------------------------------------#

# Constante des deplacements
# i et j compteurs pour parcourir la liste de liste de L -> Savoir si mur ?
# -> position initiale du chevalier
# i et j
i = 13 # numero ligne
j = 6 # numero colonne


# Liste des objets à afficher
liste_objets = ["Spike","Potion","Key_1","Key_2","Heart","Weapon","Weapon2","Diamond_1","Diamond_2","Diamond_3","Goblin","Goliath","Boss","obstacle","porte"]
affiche_objets_init(L)
affiche_objets(liste_objets)
fenetre.blit(heros,position_heros)
pygame.display.flip()


continuer = True
gagner = False
Epee = False
Arme_Boss = False
ouvert_porte = False
score = 0
vies = 10

while continuer:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False

        if event.type == KEYDOWN :
            if event.key == K_ESCAPE:
                continuer = False


            if event.key == K_DOWN:
                if L[i+1][j]!='m' and L[i+1][j]!='obstacle' and L[i+1][j]!='porte':
                    position_heros = position_heros.move(0,taille_sprite)
                    i = i + 1


            if event.key == K_UP:
                if L[i-1][j]!='m' and L[i-1][j]!='obstacle' and L[i-1][j]!='porte':
                    position_heros = position_heros.move(0,-taille_sprite)
                    i = i - 1


            if event.key == K_RIGHT:
                if L[i][j+1]!='m' and L[i][j+1]!='obstacle' and L[i][j+1]!='porte':
                    position_heros = position_heros.move(taille_sprite,0)
                    j += 1


            if event.key == K_LEFT:
                if L[i][j-1]!='m' and L[i][j-1]!='obstacle'and L[i][j-1]!='porte':
                    position_heros = position_heros.move(-taille_sprite,0)
                    j -= 1


            if L[i][j]=="E":
                vies -= 1


    if ramassage_items(i,j):
        score +=1
        print(score)
        if score == 5:
            liste_objets.remove("porte")
            L[11][14] = "H"
            ouvert_porte == True
    if fin_jeu(i,j):
        gagner = True
        continuer = False

    if passage_secret(i,j):
        i = 1
        j = 1
        position_heros = heros.get_rect()
        position_heros = position_heros.move(taille_sprite,taille_sprite)

    if passage_secret_2(i,j):
        i = 13
        j = 1
        position_heros = heros.get_rect()
        position_heros = position_heros.move(taille_sprite,taille_sprite*13)


    if ramassage_vie(i,j):
        vies += 1
    if vies == 0:
        gagner = False
        continuer = False

    if ramassage_weapon(i,j):
        Arme_Boss = True
    if touche_boss(i,j):
        if Arme_Boss == True:
            continuer = True
        else :
            gagner = False
            continuer = False

    if ramassage_weapon_2(i,j):
        Epee = True
    if touche_ennemis(i,j):
        if Epee == True:
            continuer = True
        else :
            gagner = False
            continuer = False

    if ramassage_potion(i,j):
        liste_objets.remove("obstacle")
        L[4][14] = "H"
        L[4][15] = "H"
        L[4][16] = "H"
        L[4][17] = "H"

    #Recollage
    fenetre.blit(fond_niveau,(0,0))
    fenetre.blit(heros,position_heros)
    affiche_objets(liste_objets)

    font = pygame.font.SysFont('Comic Sans MS, Arial', 25)
    texte = font.render(f"Vies : {vies}", True, (254, 255, 191)) # Utilisation du f string
    fenetre.blit(texte,(longueur_fenetre//100,largeur_fenetre//100))
    pygame.display.flip()
    #Rafraichissement
    pygame.display.flip()



if gagner:
    fond_Win = pygame.image.load(image_Win).convert_alpha()
    fond_Win = pygame.transform.scale(fond_Win,(longueur_fenetre,largeur_fenetre))
    fenetre.blit(fond_Win,(0,0))
    pygame.display.flip()
    pygame.time.wait(2000)
else :
    pygame.mixer.music.stop()
    pygame.time.wait(500)
    fond_GameOver = pygame.image.load(image_GameOver).convert_alpha()
    fond_GameOver = pygame.transform.scale(fond_GameOver,(longueur_fenetre,largeur_fenetre))
    fenetre.blit(fond_GameOver,(0,0))
    pygame.display.flip()
    pygame.time.wait(2000)
    print("perdu")



# Fermeture fenetre
##pygame.time.wait(4000)
pygame.quit()