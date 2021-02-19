import pygame #On importe tjours les package dont on a besoin
import sys #le package python utilise pour appeler la fonction exit


pygame.init() #consiste a demarrer le module pygame
screen = pygame.display.set_mode((800, 600))  # faire apparaitre une fenetre les deux paratheses consistent a grouper deux parametres en 1
pygame.display.set_caption("Echecs")

board = pygame.Surface((480, 480))  # surface occupe par les jeu a l'ecran
board.fill((175, 141, 120)) # couleur du chequier.

for x in range(0, 8, 2): # range permet de creer une plage ou une enumeration (0,1,2,3,4,5,6,7)
    for y in range(0, 8, 2): #permet de generer les cases
        pygame.draw.rect(board, (250, 240, 230), (x * 60, y * 60, 60, 60))

for x in range (1, 9, 2): #pour inserrer les carres impair
    for y in range(1, 9, 2): #idem ici
        pygame.draw.rect(board, (250, 240, 230), (x * 60, y * 60, 60, 60))


#pour maintenir la fenetre en permanance on utilise la boucle de jeu
while True: #qui est tjrs en vrai
    for event in pygame.event.get(): # permet de lister ts les evenements et de sortir de la boucle infini. cliquer sur X d'une appli la ferme
        if event.type == pygame.QUIT: # veut dire que si l'evenement match avec quelque chose a un utilisateur qui a clique le X de la fenetre
            print("Bye Bye.")
            sys.exit(0)  # permet de quitter le script. Le 0 signifie qu'il y a pas d'erreurs et un autre chiffre des erreurs

    # comment faire une reaction a clic de souri?
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event == 1:
                x, y = event.pos
                print(x, y)
        elif event.type == pygame.MOUSEBUTTONUP:
            if event == 1:
                x, y = event.pos
                print(x, y)

    screen.fill((150, 150, 150)) #couleur de fond du canevas
    screen.blit(board, board.get_rect()) #pour lier l'echequier a l'ecran
    pygame.display.update()






