# coding: utf-8
#import CombatArena #import CombatArena
#import ConfigAudio  #import Audio
#import ConfigContP1 #import ControlesP1
#import ConfigContP2 #import ControlesP2
#import Configuracion #import Config
#import Instrucciones #import Instrucciones
#from SeleccionPersonajes import MenuPersonajes #import MenuPersonajes
import pilasengine

pilas = pilasengine.iniciar()

#------MenuInicial---------------------------------------------------------------

class MenuInicial(pilasengine.escenas.Escena):
    def iniciar(self):

#-------Preparando el Fondo---------------------------------------------------

        gFondo = pilas.imagenes.cargar_grilla('Imagenes\FondoMenu.png', 12)
        fondo = pilas.actores.Animacion(gFondo, ciclica=True, velocidad= 10)
        pilas.camara.escala = 2.25
        fondo.z = 10

#-------------------Funciones de las opciones de menues---------------------------

        def Iniciar_1player():
            titulo.transparencia =[0, 100], 2
            menu.transparencia = [0, 100], 2
            pilas.escenas.MenuPersonajes()

        def Iniciar_2player():
            pilas.escenas.MenuPersonajes()

        def Menu_Instrucciones():
            pilas.escenas.Instrucciones()

        def Menu_Configuracion():
            pilas.escenas.Config()

        def Salir_Juego():
            pilas.terminar()

#---------------------Menu------------------------------------------------------

        menu = pilas.actores.Menu(
            [
                ("1 Player", Iniciar_1player),
                ("2 Players", Iniciar_2player),
                ("Instrucciones", Menu_Instrucciones),
                ("Configuracion", Menu_Configuracion),
                ("Salir", Salir_Juego),
            ])

#---------------Titulo y animacion de inicio-------------------------------------

        titulo = pilas.actores.Actor()
        titulo.imagen = "Imagenes\Titulo.png"
        titulo.transparencia=100
        menu.transparencia=100
        titulo.transparencia =[100, 0], 2
        menu.transparencia = [100, 100, 0], 2
        titulo.escala=.6
        titulo.y=60

#---------------------Salteo de animacion de inicio-------------------------

    #def actualizar(self):
    #    if (pilas.eventos.pulsa_tecla):
      #      self.titulo.transparencia=0
        #    self.menu.transparencia = 0

#------------------------------------------------------------------------------

#pilas.escenas.vincular(MenuInicial)
#pilas.escenas.vincular(MenuPersonajes)
#pilas.escenas.vincular(CombatArena)
#pilas.escenas.vincular(Instrucciones)
#pilas.escenas.vincular(Config)
#pilas.escenas.vincular(Audio)
#pilas.escenas.vincular(ControlesP1)
#pilas.escenas.vincular(ControlesP2)

#pilas.escenas.MenuInicial()


pilas.ejecutar()