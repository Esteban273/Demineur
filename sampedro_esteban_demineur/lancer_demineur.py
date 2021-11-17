### Importation des modules et de la classe Demineur
import pygame
from pygame.locals import *
import time
import classdemineur as de

#taille de la fenêtre
pygame.init()
taille = largeur, hauteur = 1200,800
fenetre = pygame.display.set_mode(taille)

#image de chargement
fond = pygame.image.load("Intro.png").convert()
fenetre.blit(fond, (0,0))
pygame.display.flip()

time.sleep(2)

#######RESTART
restart = True
while restart :
    restart = False

    #sélection niveau
    fond = pygame.image.load("fond_level.png").convert()
    fenetre.blit(fond, (0,0))
    easy = pygame.image.load("easy.png").convert()
    fenetre.blit(easy, (100,500))
    normal = pygame.image.load("normal.png").convert()
    fenetre.blit(normal, (500,500))
    hard = pygame.image.load("hard.png").convert()
    fenetre.blit(hard, (900,500))

    pygame.display.flip()

    suite = True #pour arreter le prgm apres un QUIT
    
    continuer = True #pour arreter la fenetre
    while continuer :
        for event in pygame.event.get():
            if event.type == QUIT:
                suite = False
                continuer = False
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] >= 100 and event.pos[0] <= 300 and event.pos[1] >= 500 and event.pos[1] <= 600 :
                niveau = "easy"
                continuer = False
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] >= 500 and event.pos[0] <= 700 and event.pos[1] >= 500 and event.pos[1] <= 600 :
                niveau = "normal"
                continuer = False
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] >= 900 and event.pos[0] <= 1100 and event.pos[1] >= 500 and event.pos[1] <= 600 :
                niveau = "hard"
                continuer = False

    if suite == True : #si on doit continuer
        
        #grille départ
        fond = pygame.image.load("fondnoir.png").convert()
        fenetre.blit(fond, (0,0))
    
        if niveau == "easy": #images niv easy
            orange = pygame.image.load("easy_orange.png").convert()
            jaune = pygame.image.load("easy_jaune.png").convert()
            bombe = pygame.image.load("easy_bombe.png").convert()
            num1 = pygame.image.load("easy_chiffre_1.png").convert()
            num2 = pygame.image.load("easy_chiffre_2.png").convert()
            num3 = pygame.image.load("easy_chiffre_3.png").convert()
            num4 = pygame.image.load("easy_chiffre_4.png").convert()
            num5 = pygame.image.load("easy_chiffre_5.png").convert()
            flag = pygame.image.load("easy_drapeau.png").convert_alpha()
            rien = pygame.image.load("easy_vide.png").convert()
    
            part = de.Demineur(1)

        if niveau == "normal": #images niv normal
            orange = pygame.image.load("normal_orange.png").convert()
            jaune = pygame.image.load("normal_jaune.png").convert()
            bombe = pygame.image.load("normal_bombe.png").convert()
            num1 = pygame.image.load("normal_chiffre_1.png").convert()
            num2 = pygame.image.load("normal_chiffre_2.png").convert()
            num3 = pygame.image.load("normal_chiffre_3.png").convert()
            num4 = pygame.image.load("normal_chiffre_4.png").convert()
            num5 = pygame.image.load("normal_chiffre_5.png").convert()
            flag = pygame.image.load("normal_drapeau.png").convert_alpha()
            rien = pygame.image.load("normal_vide.png").convert()

            part = de.Demineur(2)

        if niveau == "hard": #images niv hard
            orange = pygame.image.load("hard_orange.png").convert()
            jaune = pygame.image.load("hard_jaune.png").convert()
            bombe = pygame.image.load("hard_bombe.png").convert()
            num1 = pygame.image.load("hard_chiffre_1.png").convert()
            num2 = pygame.image.load("hard_chiffre_2.png").convert()
            num3 = pygame.image.load("hard_chiffre_3.png").convert()
            num4 = pygame.image.load("hard_chiffre_4.png").convert()
            num5 = pygame.image.load("hard_chiffre_5.png").convert()
            flag = pygame.image.load("hard_drapeau.png").convert_alpha()
            rien = pygame.image.load("hard_vide.png").convert()
        
            part = de.Demineur(3)

        part.init_cases()
        part.damier(orange,jaune)
        for element in part.get_damier_multi():
            fenetre.blit(part.get_damier_multi()[element], element)

        pygame.display.flip()

        #attente du premier clique
        continuer = True #pour arreter la fenetre
        while continuer :
            for event in pygame.event.get():
                if event.type == QUIT:
                    suite = False
                    continuer = False
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    case = (event.pos[0],event.pos[1])
                    case = part.case_simple(case)
                    if case in part.get_dico():
                        continuer = False

        if suite == True : #si on doit continuer
            
            part.cases_nuls(case)
            part.lesbombes()
            part.chiffres()

            ##### Zone de fonction pour révéler cases #######
            def couleur(case,dico):
                """Fonction qui suivant la valeur (de la clé de coordonnée) dans dico du démineur,
                révèle la case nécessaire (image uploader auparavant)"""
                if dico[case] == 0:
                    fenetre.blit(rien, case)
                if dico[case] == "bombe" :
                    fenetre.blit(bombe, case)
                if dico[case] == 1 :
                    fenetre.blit(num1, case)
                if dico[case] == 2 :
                    fenetre.blit(num2, case)
                if dico[case] == 3 :
                    fenetre.blit(num3, case)
                if dico[case] == 4 :
                    fenetre.blit(num4, case)
                if dico[case] == 5 :
                    fenetre.blit(num5, case)
    

            def decouvrir(case,part,liste_visite):
                """fonction qui repre,d l'algorithme de Flutfile qui permet de découvrir toute une zone de case nul jusqu'à rencontrer des chiffres"""
                if case in part.get_dico():
                    if case not in liste_visite :
                        couleur((case[0]*part.get_multi(),case[1]*part.get_multi()),part.multi_pixel())
                        liste_visite.append(case)
                        if part.get_dico()[case] == 0:
                            decouvrir((case[0]+1,case[1]),part,liste_visite)
                            decouvrir((case[0],case[1]+1),part,liste_visite)
                            decouvrir((case[0]-1,case[1]),part,liste_visite)
                            decouvrir((case[0],case[1]-1),part,liste_visite)
                            decouvrir((case[0]+1,case[1]+1),part,liste_visite)
                            decouvrir((case[0]-1,case[1]+1),part,liste_visite)
                            decouvrir((case[0]-1,case[1]-1),part,liste_visite)
                            decouvrir((case[0]+1,case[1]-1),part,liste_visite)

            def flagflag(case,part,liste_visite,liste_drap):
                """fonction qui permet d'ajouter un drapeau sur une case non révélé ou de le retiré"""
                if case not in liste_visite and case not in liste_drap :
                    fenetre.blit(flag, (case[0]*part.get_multi(),case[1]*part.get_multi()))
                    liste_drap.append(case)
        
                elif case in liste_drap :
                    fenetre.blit(part.get_damier()[case], (case[0]*part.get_multi(),case[1]*part.get_multi()))
                    new_liste_drap = []
                    for element in liste_drap :
                        if element != case:
                            new_liste_drap.append(element)
                    liste_drap = new_liste_drap
                return liste_drap

            ##########################################

            liste_visite = []
            decouvrir(case,part,liste_visite)
            pygame.display.flip()  
            liste_drap = []

            ######## Etape ajout chronomètre
            TpsZero = pygame.time.get_ticks() ## Départ

            def temps():
                """fonction qui récupère le temps"""
                seconds = (pygame.time.get_ticks() - TpsZero) // 1000
                minu = seconds // 60
                sec = seconds % 60
                return (minu,sec)

            police = pygame.font.Font(None,72)

            def texte(tps):
                """fonction qui prepare l'ecriture du chrono"""
                chiffre = [0,1,2,3,4,5,6,7,8,9]
                if tps[0] in chiffre :
                    minu = "0" + str(tps[0])
                else :
                    minu = str(tps[0])
                if tps[1] in chiffre :
                    sec = "0" + str(tps[1])
                else :
                    sec = str(tps[1])
                chrono = minu + "'" + sec
                return (police.render(chrono,True,pygame.Color("white")),chrono)

            cache_chrono = pygame.image.load("cache_chrono.png").convert()#permet de cacher le chrono afin de ne pas empiler les images

            #nombre de drapeau restant (info sur le coté)
            decompte = pygame.image.load("normal_drapeau.png").convert_alpha()
            fenetre.blit(decompte, (1050,400))
        
            ##### afficher le nombre de drapeau restant
            nombre_drap = part.get_bombe() - len(liste_drap)
            aff_drap = police.render(str(nombre_drap),True,pygame.Color("white"))
            fenetre.blit(aff_drap, (1100,400))
            pygame.display.flip()

            #### bouton restart
            bout_restart = pygame.image.load("restart.png").convert()
            fenetre.blit(bout_restart, (1025,700))
            pygame.display.flip()
            
            ######
            continuer = True #pour arreter la fenetre
            while continuer :
                fenetre.blit(cache_chrono, (1050,200))
                chrono = texte(temps())
                fenetre.blit(chrono[0], (1050,200))
                pygame.display.flip()
                ###
                for event in pygame.event.get():
                    if event.type == QUIT:
                        suite = False
                        continuer = False
                    ### decouvrir case
                    if event.type == MOUSEBUTTONDOWN and event.button == 1: #si clique gauche
                        case = (event.pos[0],event.pos[1])
                        case = part.case_simple(case)
                        if case in part.get_dico() and case not in liste_drap :
                            if part.get_dico()[case] == "bombe":
                                continuer = False
                                decouvrir(case,part,liste_visite)
                                for element in part.multi_pixel():
                                    if part.multi_pixel()[element] == "bombe":
                                        couleur(element,part.multi_pixel())
                                        pygame.display.flip()
                                        #tps de vision des bombes
                                        if niveau == "easy":
                                            time.sleep(0.1)
                                        if niveau == "normal":
                                            time.sleep(0.05)
                                        if niveau == "hard":
                                            time.sleep(0.01)
                                time.sleep(1)
                                ### Affichage fin
                                fond = pygame.image.load("fond.png").convert()
                                fenetre.blit(fond, (0,0))
                                phrase = "Tu as perdu au niveau " + niveau + " ."
                                defaite = police.render(phrase,True,pygame.Color("black"))
                                fenetre.blit(defaite, (200,375))
                                pygame.display.flip()
                    
                            else:
                                decouvrir(case,part,liste_visite)
                                pygame.display.flip()
                                if len(liste_visite) == part.get_nbr_cases():
                                    continuer = False
                                    time.sleep(1)
                                    ### Affichage fin
                                    fond = pygame.image.load("fond.png").convert()
                                    fenetre.blit(fond, (0,0))
                                    phrase = "Tu as gagné au niveau " + niveau + " en " + chrono[1] + " ."
                                    victoire = police.render(phrase,True,pygame.Color("black"))
                                    fenetre.blit(victoire, (200,375))
                                    pygame.display.flip()
                    ### Drapeau          
                    if event.type == MOUSEBUTTONDOWN and event.button == 3: #si clique droit
                        case = (event.pos[0],event.pos[1])
                        case = part.case_simple(case)
                        if case in part.get_dico():
                            liste_drap = flagflag(case,part,liste_visite,liste_drap)
                            nombre_drap = part.get_bombe() - len(liste_drap)
                            aff_drap = police.render(str(nombre_drap),True,pygame.Color("white"))
                            fenetre.blit(cache_chrono, (1100,400))
                            fenetre.blit(aff_drap, (1100,400))
                            pygame.display.flip()
                    ### restart
                    if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] >= 1025 and event.pos[0] <= 1175 and event.pos[1] >= 700 and event.pos[1] <= 775 :
                        continuer = False
                        suite = False
                        restart = True


        if suite == True:

            bout_quit = pygame.image.load("quit.png").convert()
            fenetre.blit(bout_quit, (300,525))
            fenetre.blit(bout_restart, (750,525))
            pygame.display.flip()
            
            continuer = True #pour arreter la fenetre
            while continuer :
                for event in pygame.event.get():
                    if event.type == QUIT:
                        continuer = False
                    if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] >= 300 and event.pos[0] <= 450 and event.pos[1] >= 525 and event.pos[1] <= 600 :
                        continuer = False
                    if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] >= 750 and event.pos[0] <= 900 and event.pos[1] >= 525 and event.pos[1] <= 600 :
                        continuer = False
                        restart = True
