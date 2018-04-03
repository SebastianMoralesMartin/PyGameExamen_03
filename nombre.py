#encoding: UTF-8
# Sebastian Morales Martin
# Examen Practico 30%

import pygame
# si esta cansado esto ;-(
# Altura de las letras: 30 pixeles
# Ancho de las letras: 20 pixeles
# espacios entre letras: 5 pixeles
#separacion de palabra: 25 pixeles
#La siguiente lista, conformada por 304 valores imprimen en pantalla el siguiente nombree: SEBASTIÁN MORALES MARTÍN
listaNumeros = [60,90,70,95,50,95,60,90,50, 95,70, 115,70, 115,60,120, 60, 120,50,
                115,75, 120,75, 90,75,120,95, 120,75, 105,95, 105,75, 90,95,
                90,100, 90,100, 120,100, 90,115,100,115,100,100,100,100,100,120,
                110,120, 110,100,120,125, 120,135,90,135,90,145,120,160,90,170,
                95,150,95,160,90,150, 95,170, 115,170, 115,160,120, 160, 120,150,
                115,185,90,185,120,175,90,195,90,210,90,210,120,205,90,215,90,205,
                120,215,120,225,120,235,90,235,90,245,120,250,120,250,90,250,90,270,
                120,270,120,270,90,235,85,245,75,295,120,295,90,295,90,305,100,305,
                100,315,90,315,90,315,120,320,105,330,90,320,105,330,120,330,120,340,
                105,330,90,340,105,345,120,345,90,345,90,365,100,365,100,345,105,345,
                105,365,120,370,120,380,90,380,90,390,120,395,90,395,120,395,120,415,
                120,420,120,420,90,420,120,440,120,420,105,440,105,420,90,440,90,465,
                95,455,90,455,90,445,95,445,95,465,115,465,115,455,120,455,120,445,115,
                490,120,490,90,490,90,500,100,500,100,510,90,510,90,510,120,515,120,525,
                90,525,90,535,120,540,120,540,90,540,90,560,100,560,100,540,105,540,105,
                560,120,575,120,575,90,565,90,585,90,600,120,600,90,595,90,605,90,595,
                120,605,120,600,85,610,75,620,120,620,90,620,90,640,120,640,120,640,90]
# Dimensiones de la pantalla
ANCHO = 690
ALTO = 210
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255]
VERDE_BANDERA = (0, 122, 0)
ROJO = (255, 0, 0)
NEGRO = (0, 0, 0)

def dibujarNombre(ventana):
    contador1 = 0
    contador2 = 1
    contador3 = 2
    contador4 = 3
    for numero in range(len(listaNumeros)//4):
        pygame.draw.line(ventana,ROJO, (listaNumeros[contador1], listaNumeros[contador2]),(listaNumeros[contador3],listaNumeros[contador4]),2)
        contador1 += 4
        contador2 += 4
        contador3 += 4
        contador4 += 4
# Estructura básica de un programa que usa pygame para dibujar
def dibujar():


    # Inicializa el motor de pygame
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))    # Crea la ventana de dibujo
    reloj = pygame.time.Clock()     # Para limitar los fps
    termina = False                 # Bandera para saber si termina la ejecución

    while not termina:              # Ciclo principal
        # Procesa los eventos que recibe el programa
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

        # Borrar pantalla
        ventana.fill(NEGRO)
        pygame.display.set_caption("30% de mi EXAMEN esta aqui XD")

        # Dibujar, aquí haces todos los trazos que requieras
        dibujarNombre(ventana)


        pygame.display.flip()   # Actualiza trazos
        reloj.tick(40)          # 40 fps

    # Después del ciclo principal
    pygame.quit()   # termina pygame


def main():
    dibujar()



main()

print('¡¡¡La lista tiene un total de :',len(listaNumeros),'números!!!')

