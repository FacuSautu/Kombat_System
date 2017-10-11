# coding: utf-8
import pilasengine

pilas = pilasengine.iniciar()

class Instrucciones(pilasengine.escenas.Escena):
    def iniciar(self):
        gFondo = pilas.imagenes.cargar_grilla('Imagenes\FondoMenu.png', 12)
        fondo = pilas.actores.Animacion(gFondo, ciclica=True, velocidad= 10)
        pilas.camara.escala=2.25
        fondo.z=-10
        
        Ins = pilas.actores.Texto("Kombat System es un juego de pelea donde cada personaje puede golpear, bloquear, moverse hacia los lados, saltar y, ademas, tiene una Habilidad Unica, la cual puede usarse una vez cargada la barra de energia,a travez de golpear al contrincante.")
        Ins.ancho=600
        Ins.escala=.8
        Ins.y=-50
        Ins.color= "grisclaro"
        
        volver = pilas.actores.Texto("Pulsa cualquier tecla para volver al menu")
        volver.escala=.5
        volver.x=-150
        volver.y=-220
        volver.color= "grisclaro"
        
        titulo = pilas.actores.Actor()
        titulo.imagen = "Imagenes\Titulo.png"
        titulo.escala=.6
        titulo.y=60
    
    def actualizar(self):
        def Volver(self, evento):
            #pilas.escenas.MenuInicial()
            print("HOLA")
        
        self.pilas.eventos.pulsa_tecla.conectar(Volver)
        
#-------------------Vinculacion de escenas------------------------
        
pilas.escenas.vincular(MenuInicial)
pilas.escenas.vincular(MenuPersonajes)
pilas.escenas.vincular(CombatArena)
pilas.escenas.vincular(Instrucciones)
pilas.escenas.vincular(Config)
pilas.escenas.vincular(Audio)
pilas.escenas.vincular(ControlesP1)
pilas.escenas.vincular(ControlesP2)

pilas.escenas.Instrucciones()

pilas.ejecutar()