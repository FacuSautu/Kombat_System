# coding: utf-8
import pilasengine

pilas = pilasengine.iniciar()

#------MenuInicial-------------------------------------------------------------
class MenuInicial(pilasengine.escenas.Escena):
    def iniciar(self):
        gFondo = pilas.imagenes.cargar_grilla('Imagenes\FondoMenu.png', 12)
        fondo = pilas.actores.Animacion(gFondo, ciclica=True, velocidad= 10)
        pilas.camara.escala=2.25
        fondo.z=10
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
        
        menu = pilas.actores.Menu(
            [
                ("1 Player", Iniciar_1player),
                ("2 Players", Iniciar_2player),
                ("Instrucciones", Menu_Instrucciones),
                ("Configuracion", Menu_Configuracion),
                ("Salir", Salir_Juego),
            ])

        titulo = pilas.actores.Actor()
        titulo.imagen = "Imagenes\Titulo.png"
        titulo.transparencia=100
        menu.transparencia=100
        titulo.transparencia =[100, 0], 2
        menu.transparencia = [100, 100, 0], 2
        titulo.escala=.6
        titulo.y=60
        
#------------------------------------------------------------------------------

pilas.escenas.vincular(MenuInicial)
pilas.escenas.vincular(MenuPersonajes)
pilas.escenas.vincular(CombatArena)
pilas.escenas.vincular(Instrucciones)
pilas.escenas.vincular(Config)

pilas.escenas.MenuInicial()


pilas.ejecutar()