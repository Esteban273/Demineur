class Demineur:
    """Classe qui permet de créer un démineur facilement. Elle permet de manier les attributs de clui-ci sans difficultés.
Attributs :
    diff : int
        permet de connaitre le niveau de difficulté choisi par le joueur (1 : easy, 2 : normal, 3 : hard)
        Initialise le nombre de case (longueur*hauteur), le nombre de bombes, un dico, le multiplicateur de pixel (taille affichage) et le nombre de case à découvrir au premier clique.
Méthodes :
    get_bombe : donne le nombre de bombe dans le niveau
    get_dico : donne le dictionnaire qui pour chaque clé (coordonée d'une case) à pour valeur le numéro ou la bombe du démineur
    get_multi : donne le multiplicateur de pixel du niveau pour avoir les images à la bonne taille
    get_nbr_cases : donne le nombre de cases dans un niveau
    case_simple : permet de reduire les coordonnées du clique du joueur à des coordonnées de base
    init_case : permet d'initialiser les cases du démineur dans le dico
    multi_pixel : permet de renvoyer le dictionnaire avec les coordonnées multiplier afin d'obtenir la bonne taille d'image
    damier : permet de creer le damier qui recouvrira les nombres et bombes sous la forme d'un dictionnaire pour que chaque case est sa couleur (self.couleur_case)
    get_damier : retourne le dictionnaire du damier
    get_damier_multi : retourn le dictionnaire du damier à la bonne taille d'image
    case_nuls : ajouter des cases nuls dans le dico,
        permet de découvrir un certain nombre de case lors du premier clique du joueur, ce sont que des cases nuls afin d'obtenir les chiffres sur les bords de la zone
    lesbombes : permet d'ajouter le placement des bombes dans le dictionnaire
    chiffres : permet de placer les chiffres qui sont autour des bombes dans le dictionnaire
"""
    def __init__(self,diff):
        """Attributs : diff
                permet de créer un démineur en fonction de sa difficulté"""
        if diff == 1 :
            self.longueur = 10
            self.hauteur = 8
            self.bombes = 12
            self.dico = {}
            self.multiplicateur = 100
            self.case_nul = 20
            
        if diff == 2 :
            self.longueur = 20
            self.hauteur = 16
            self.bombes = 50
            self.dico = {}
            self.multiplicateur = 50
            self.case_nul = 40
            
        if diff == 3 :
            self.longueur = 40
            self.hauteur = 32
            self.bombes = 180
            self.dico = {}
            self.multiplicateur = 25
            self.case_nul = 60

        self.couleur_case = {}

    def get_bombe(self) :
        """Retourne le nombre de bombes"""
        return self.bombes
    
    def get_dico(self):
        """retourne le dictionnaire des cases"""
        return self.dico

    def get_multi(self):
        """retourne le multiplicateur de pixel pour les images"""
        return self.multiplicateur

    def get_nbr_cases(self):
        """retourne le nombre de cases du niveau"""
        return self.longueur*self.hauteur - self.bombes

    def case_simple(self,case):
        """permet de reduire les coordonnées à des coordonnées simple comme dans le self.dico"""
        return (case[0]//self.multiplicateur,case[1]//self.multiplicateur)

    def init_cases(self):
        """permet d'initialier le self.dico"""
        for i in range(self.longueur):
            for k in range(self.hauteur):
                self.dico[(i,k)] = (None)

    def multi_pixel(self):
        """permet de revoyer le self.dico mais avec les coorddonée de taille des images"""
        new_dico = {}
        for case in self.dico :
            new_dico[(case[0]*self.multiplicateur,case[1]*self.multiplicateur)] = self.dico[case]
        return new_dico

    def damier(self,c1,c2):
        """initialise un dico avec le damier qui recouvre les bombes"""
        for element in self.dico :
            if element[1]%2 == 0:
                if element[0]%2 == 0:
                    self.couleur_case[element] = c1
                else :
                    self.couleur_case[element] = c2
            else :
                if element[0]%2 == 0:
                    self.couleur_case[element] = c2
                else :
                    self.couleur_case[element] = c1

    def get_damier(self):
        """retourne le dictionnaire du damier"""
        return self.couleur_case

    def get_damier_multi(self):
        """retourne le dictionnaire du damier avec les coordonnée de la taille des images"""
        new_dico = {}
        for case in self.couleur_case :
            new_dico[(case[0]*self.multiplicateur,case[1]*self.multiplicateur)] = self.couleur_case[case]
        return new_dico

    
    def cases_nuls(self,prem_case):
        """permet de créer une zone de case nul au début de la partie, dans self.dico"""
        import random
        self.dico[prem_case] = 0
        liste = [(prem_case[0]+1,prem_case[1]),(prem_case[0]-1,prem_case[1]),(prem_case[0],prem_case[1]+1),(prem_case[0],prem_case[1]-1),(prem_case[0]+1,prem_case[1]+1),(prem_case[0]-1,prem_case[1]+1),(prem_case[0]+1,prem_case[1]-1),(prem_case[0]-1,prem_case[1]-1)]
        for el in liste:
            if el in self.dico :
                self.dico[el] = 0
        case_actu = prem_case
        for i in range(self.case_nul):
            k = random.randint(1,4)
            if k == 1:
                new_case = (case_actu[0]+1,case_actu[1])
                if new_case in self.dico:
                    self.dico[new_case] = 0
                    case_actu = new_case
            if k == 2:
                new_case = (case_actu[0]-1,case_actu[1])
                if new_case in self.dico:
                    self.dico[new_case] = 0
                    case_actu = new_case
            if k == 3:
                new_case = (case_actu[0],case_actu[1]+1)
                if new_case in self.dico:
                    self.dico[new_case] = 0
                    case_actu = new_case
            if k == 4:
                new_case = (case_actu[0],case_actu[1]-1)
                if new_case in self.dico:
                    self.dico[new_case] = 0
                    case_actu = new_case
                        
    def lesbombes(self):
        """permet d'ajouter l'emplacement des bombes dans le self.dico"""
        import random
        temps = self.bombes
        while temps != 0:
            x = random.randint(0,self.longueur-1)
            y = random.randint(0,self.hauteur-1)
            if self.dico[(x,y)] == None :
                self.dico[(x,y)] = "bombe"
                temps -= 1
                
    def chiffres(self):
        """permet d'ajouter les chiffres qui sont autour des bombes dans self.dico"""
        for i in range(self.longueur):
            for k in range(self.hauteur):
                if self.dico[(i,k)] != "bombe":
                    liste = [(i-1,k-1),(i,k-1),(i+1,k-1),(i-1,k),(i+1,k),(i-1,k+1),(i,k+1),(i+1,k+1)]
                    list2 = []
                    for element in liste :
                        if element in self.dico :
                            list2.append(element)
                    tot = 0
                    for el in list2:
                        if self.dico[el] == "bombe" :
                            tot += 1
                    self.dico[(i,k)] = tot
