# coding: utf-8
import pilasengine

pilas = pilasengine.iniciar()

class Config(pilasengine.escenas.Escena):
    def iniciar(self):
        gFondo = pilas.imagenes.cargar_grilla('Imagenes\FondoMenu.png', 12)
        fondo = pilas.actores.Animacion(gFondo, ciclica=True, velocidad= 10)
        pilas.camara.escala=2.25
        fondo.z=10
        
        def Menu_Audio():
            pilas.escenas.Audio()
            
        def Menu_Controles1():
            pilas.escenas.ControlesP1()
            
        def Menu_Controles2():
            pilas.escenas.ControlesP2()
        
        configuracion = pilas.actores.Menu(
            [
                ("Audio", Menu_Audio),
                ("Controles player 1", Menu_Controles1),
                ("Controles player 2", Menu_Controles2),
            ])
        
        titulo = pilas.actores.Actor()
        titulo.imagen = "Imagenes\Titulo.png"
        titulo.escala=.6
        titulo.y=60


pilas.escenas.vincular(Config)
pilas.escenas.vincular(Audio)
pilas.escenas.vincular(ControlesP1)
pilas.escenas.vincular(ControlesP2)
pilas.escenas.Config()

pilas.ejecutar()