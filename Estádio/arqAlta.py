# -*- coding: utf-8 -*- 

from math import cos
from math import pi
from math import sin
import timeit
#import numpy
import ctypes
import random
from sys import argv
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

global esqdir
global cimabaixo
global aux1
global aux2
global angulo


esqdir = 1.7
cimabaixo = 5.1
aux1 = 0
aux2 = 0
aux3 = 0
aux4 = 0
angulo = 120


def degrau():
    glPushMatrix()
    glScalef(2, 80, 1.0)
    glutSolidCube(0.5)
    glPopMatrix()

def degrau2():
    glPushMatrix()
    glScalef(2, 700, 1.0)
    glutSolidCube(0.5)
    glPopMatrix()

def haste():
    # Coluna
    glPushMatrix()
    glColor3f(0.1,0.1,0.1)
    glRotate(90, 1.0, 0.0, 0.0)
    glTranslate(-6.4,3.6,-7.5)
    glutSolidCylinder(0.05, 6.0, 40, 10)
    glPopMatrix()

    # Haste
    glPushMatrix()
    glColor3f(0.3,0.3,0.3)
    glRotate(90, 1.0, 0.0, 0.0)
    glRotate(-60, 0.0, 1.0, 0.0)
    glTranslate(-9,3.6,1)
    glutSolidCylinder(0.03, 1.0, 40, 10)
    glPopMatrix()

def janela():

    glPushMatrix()
    glColor3f(0,0,0)
    glTranslate(-6.9,6.3,2.85)
    glScalef(1,1,1.4)
    glutSolidCube(1)  
    glPopMatrix()

    glPushMatrix()
    glColor3f(0.8,0.8,0.8)
    glTranslate(-6.8,6.3,2.85)
    glScalef(1,1,1.4)
    glutSolidCube(0.9)  
    glPopMatrix()

def muroDireito():
    # MURO
    glPushMatrix()
    glColor3f(1,1,1)
    glScalef(0.1,1,2.5)
    glTranslate(-100,5.3,-3.3)
    glutSolidCube(1)
    glPopMatrix()

    glPushMatrix()
    glColor3f(1,1,1)
    glTranslate(-10,6,-9.6)
    glutSolidCylinder(0.02, 2.6, 40, 10)
    glPopMatrix()

    glPushMatrix()
    glColor3f(1,1,1)
    glRotate(90, 1.0, 0.0, 0.0)
    glTranslate(-10,-8.3,-6)
    glutSolidCylinder(0.04, 0.5, 40, 10)
    glPopMatrix()

def muroEsquerdo():
  
    glPushMatrix()
    glColor3f(1,1,1)
    glScalef(0.1,1,2.5)
    glTranslate(-100,5.3,3.3)
    glutSolidCube(1)
    glPopMatrix()

    glPushMatrix()
    glColor3f(1,1,1)
    glTranslate(-10,6,7)
    glutSolidCylinder(0.02, 2.6, 40, 10)
    glPopMatrix()

    glPushMatrix()
    glColor3f(1,1,1)
    glRotate(90, 1.0, 0.0, 0.0)
    glTranslate(-10,8.3,-6)
    glutSolidCylinder(0.04, 0.5, 40, 10)
    glPopMatrix()


def corrimao():
    # CORRIMÃO

    glPushMatrix()
    glColor3f(0.3,0.3,0.3)
    glTranslate(-0.6,3.5,17)
    glutSolidCylinder(0.02, 3.0, 40, 10)
    glPopMatrix()

    glPushMatrix()
    glColor3f(0.8,0.8,0.8)
    glTranslate(-0.6,3.4,17)
    glutSolidCylinder(0.02, 3.0, 40, 10)
    glPopMatrix()

    glPushMatrix()
    glColor3f(0.8,0.8,0.8)
    glTranslate(-0.6,3.3,17)
    glutSolidCylinder(0.02, 3.0, 40, 10)
    glPopMatrix()

    glPushMatrix()
    glColor3f(0.3,0.3,0.3)
    glTranslate(-0.6,3.2,17)
    glutSolidCylinder(0.02, 3.0, 40, 10)
    glPopMatrix()

    glPushMatrix()
    glColor3f(0.3,0.3,0.3)
    glRotate(90, 1.0, 0.0, 0.0)
    glTranslate(-0.6,18,-3.5)
    glutSolidCylinder(0.02, 0.5, 40, 10)
    glPopMatrix()

def desenho():

    # Parte Baixa

    glPushMatrix()
    glRotatef(90, 1.0, 0.0, 0.0)
    contador = 0
    while contador <= 4:
        if contador%2==0:
            glColor3f(0.1,0.1,0.1)
            degrau()
            glTranslate(0.5,0,0.2)
        else:
            glColor3f(1,1,1)
            degrau()
            glTranslate(0.5,0,0.2)
        contador+=1
    glPopMatrix()

    # Divisão

    glPushMatrix()
    glRotatef(90, 1.0, 0.0, 0.0)
    glColor3f(1,1,1)
    glScalef(0.1,80,7)
    glTranslate(-6,0,-0.2)
    glutSolidCube(0.5)
    glPopMatrix()

    # Piso parte alta

    glPushMatrix()
    glColor3f(0.5,0.5,0.5)
    glScalef(2.5,1,1)
    glTranslate(-0.75,2,0)
    glRotatef(90, 1.0, 0.0, 0.0)
    degrau()
    glPopMatrix()

    # Parte Alta Esquerda

    glPushMatrix()
    glTranslate(-9.5,4.6,-15)
    glRotatef(90, 1.0, 0.0, 0.0)
    contador = 0
    glScalef(1, 0.3, 1)
    while contador <= 12:
        if contador%2==0:
            glColor3f(1,1,1)
            degrau()
            glTranslate(0.5,0,0.2)
        else:
            glColor3f(0.1,0.1,0.1)
            degrau()
            glTranslate(0.5,0,0.2)
        contador+=1
    glPopMatrix()

    # Parte Alta Esquerda Com Sobra

    glPushMatrix()
    glTranslate(-9.5,4.6,8)
    glRotatef(90, 1.0, 0.0, 0.0)
    contador = 0
    glScalef(1, 0.05, 1)
    while contador <= 12:
        if contador <= 6:
            if contador%2==0:
                glColor3f(1,1,1)
                degrau()
                glTranslate(0.5,0,0.2)
            else:
                glColor3f(0.1,0.1,0.1)
                degrau()
                glTranslate(0.5,0,0.2)
        else:
            if contador%2==0:
                glColor3f(1,1,1)
                degrau2()
                glTranslate(0.5,0,0.2)
            else:
                glColor3f(0.1,0.1,0.1)
                degrau2()
                glTranslate(0.5,0,0.2)
        contador+=1
    glPopMatrix()



    # Parte Alta Direita

    glPushMatrix()
    glTranslate(-9.5,4.6,15)
    glRotatef(90, 1.0, 0.0, 0.0)
    contador = 0
    glScalef(1, 0.3, 1)
    while contador <= 12:
        if contador%2==0:
            glColor3f(1,1,1)
            degrau()
            glTranslate(0.5,0,0.2)
        else:
            glColor3f(0.1,0.1,0.1)
            degrau()
            glTranslate(0.5,0,0.2)
        contador+=1
    glPopMatrix()

    # Parte Alta Direita Com Sobra

    glPushMatrix()
    glTranslate(-9.5,4.6,-8)
    glRotatef(90, 1.0, 0.0, 0.0)
    contador = 0
    glScalef(1, 0.05, 1)
    while contador <= 12:
        if contador <= 6:
            if contador%2==0:
                glColor3f(1,1,1)
                degrau()
                glTranslate(0.5,0,0.2)
            else:
                glColor3f(0.1,0.1,0.1)
                degrau()
                glTranslate(0.5,0,0.2)
        else:
            if contador%2==0:
                glColor3f(1,1,1)
                degrau2()
                glTranslate(0.5,0,0.2)
            else:
                glColor3f(0.1,0.1,0.1)
                degrau2()
                glTranslate(0.5,0,0.2)
        contador+=1
    glPopMatrix()

    # Cabines de imprensa

        # BLOCO
    glPushMatrix()
    glColor3f(0.9,0.9,0.9)
    glTranslate(-8.0,5,-0.15)
    glScalef(1,1.5,2.6)
    glutSolidCube(3)  
    glPopMatrix()

        # JANELAS
    glPushMatrix()
    contador = 0
    while contador <= 4:
        janela()
        glTranslate(0,0,-1.5)
        contador+=1
    glPopMatrix()
        
        # HASTES
    glPushMatrix()
    contador = 0
    while contador <= 5:
        haste()
        glTranslate(0,0,-1.5)
        contador+=1
    glPopMatrix()

        # TETO
    glPushMatrix()
    glColor3f(0.1,0.1,0.1)
    glTranslate(-4.2,7.4,0)
    glScalef(1.5,0.05,2.7)
    glutSolidCube(3)  
    glPopMatrix()
    
    # CORRIMÕES
    glPushMatrix()
    contador = 0
    while contador <= 25:
        corrimao()
        glTranslate(0,0,-1.5)
        contador+=1
    glPopMatrix()

    # MURO DIR
    glPushMatrix()
    contador = 0
    while contador <= 8:
        muroDireito()
        glTranslate(0,0,-1.5)
        contador+=1
    glPopMatrix()

    glPushMatrix() 
    glTranslate(3.5,-1.5,2.8) 
    #glScalef(5,1,1)
    muroDireito()
    glColor3f(1,0,0) 
    glPopMatrix()

    # MURO ESQ
    glPushMatrix()
    contador = 0
    while contador <= 8:
        muroEsquerdo()
        glTranslate(0,0,1.5)
        contador+=1
    glPopMatrix()

    glPushMatrix() 
    glTranslate(3.5,-1.5,-2.8) 
    #glScalef(5,1,1)
    muroEsquerdo()
    glColor3f(1,0,0) 
    glPopMatrix()

    
    # Piso Parte alta
    #glPushMatrix()
    #glColor3f(1,0,0)
    #glScalef(1,1,20)
    #glutSolidCube(2)  
    #glPopMatrix()

def iluminacao_da_cena():
    global aux1
    luzAmbiente=[0.2,0.2,0.2,1.0]
    luzDifusa=[0.7,0.7,0.7,1.0]  # ; // "cor"
    luzEspecular = [1.0, 1.0, 1.0, 1.0]  #;// "brilho"
    posicaoLuz=[aux1, 50.0, 50.0, 1.0]

    #Capacidade de brilho do material
    especularidade=[1.0,1.0,1.0,1.0]
    especMaterial = 60;

    # Especifica que a cor de fundo da janela será branca
    glClearColor(0.0, 0.0, 0.0, 0.0)

    # Habilita o modelo de colorização de Gouraud
    glShadeModel(GL_SMOOTH)

    #  Define a refletância do material
    glMaterialfv(GL_FRONT,GL_SPECULAR, especularidade)
    #  Define a concentração do brilho
    glMateriali(GL_FRONT,GL_SHININESS,especMaterial)

    # Ativa o uso da luz ambiente
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, luzAmbiente)

    # Define os parâmetros da luz de número 0
    glLightfv(GL_LIGHT0, GL_AMBIENT, luzAmbiente)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, luzDifusa )
    glLightfv(GL_LIGHT0, GL_SPECULAR, luzEspecular )
    glLightfv(GL_LIGHT0, GL_POSITION, posicaoLuz )

    # Habilita a definição da cor do material a partir da cor corrente
    glEnable(GL_COLOR_MATERIAL)
    # Habilita o uso de iluminação
    glEnable(GL_LIGHTING)
    # Habilita a luz de número 0
    glEnable(GL_LIGHT0)
    # Habilita o depth-buffering
    glEnable(GL_DEPTH_TEST)


def tela():

    global angulo
    
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Limpar a tela
    glClearColor(0.0, 0.0,0.0, 0.0) # Limpa a janela com a cor especificada
    glMatrixMode(GL_PROJECTION) # Muda a matriz de projeçao
    glLoadIdentity()# carrega a matriz identidade

    gluPerspective(angulo,1,0.1,500) # Especifica a projeção perspectiva
    glMatrixMode(GL_MODELVIEW) # Especifica sistema de coordenadas do modelo
    glLoadIdentity() # Inicializa sistema de coordenadas do modelo

    gluLookAt(sin(esqdir) * 10, 0 + cimabaixo ,cos(esqdir) * 10, aux1,aux2,0, 0,1,0) # Especifica posição do observador e do alvo
    #iluminacao_da_cena()
    glEnable(GL_DEPTH_TEST) # verifica os pixels que devem ser plotados no desenho 3d

    desenho()                    
    glFlush()                    # Aplica o desenho

# Função callback chamada para gerenciar eventos de teclas normais 
def Teclado (tecla, x, y):
    global aux1
    global aux2
    
    if tecla==chr(27): # ESC ?
        sys.exit(0)

    if tecla == b'a':  # A
        aux1 = aux1 - 2
    
    if tecla == b's': # S
        aux1 = aux1 + 2
        
    if tecla == b'w': # W
        aux2 = aux2 + 2

    if tecla == b'z': # Z
        aux2 = aux2 - 2
    tela()
    glutPostRedisplay()

# Função callback chamada para gerenciar eventos de teclas especiais
def TeclasEspeciais (tecla, x, y):
    global esqdir
    global cimabaixo
    
    if tecla == GLUT_KEY_LEFT:
        esqdir = esqdir - 0.1
    elif tecla == GLUT_KEY_RIGHT:
        esqdir = esqdir + 0.1
    elif tecla == GLUT_KEY_UP:
        cimabaixo = cimabaixo + 0.05
    elif tecla == GLUT_KEY_DOWN:
        cimabaixo = cimabaixo - 0.05
    
    tela()
    glutPostRedisplay()   

# Função callback chamada para gerenciar eventos do mouse
def ControleMouse(button, state, x, y):
    global angulo
    if (button == 3):
        if (state == GLUT_DOWN): 
            angulo -= 2
        
    if (button == 4):
        if (state == GLUT_DOWN):   # Zoom-out
            angulo += 2
    print angulo
    tela()
    glutPostRedisplay()

glutInit(argv)
glutInitDisplayMode(GLUT_RGBA | GLUT_DEPTH)
glutInitWindowSize(1024,800)
glutCreateWindow("Arquibancada Alta")
distancia = 20
glutDisplayFunc(tela)
glutMouseFunc(ControleMouse)
glutKeyboardFunc (Teclado)
glutSpecialFunc (TeclasEspeciais)
glutMainLoop()  # Inicia o laço de eventos da GLUT



