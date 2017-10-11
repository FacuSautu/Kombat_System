# coding: utf-8
import pilasengine

pilas = pilasengine.iniciar()

class Audio(pilasengine.escenas.Escena):
    def iniciar(self):
        gFondo = pilas.imagenes.cargar_grilla('Imagenes\FondoMenu.png', 12)
        fondo = pilas.actores.Animacion(gFondo, ciclica=True, velocidad= 10)
        pilas.camara.escala=2.25
        fondo.z=-10
        
        subtitulo = pilas.actores.Texto("Audio")
        subtitulo.y=80
        contr = pilas.actores.Texto("General\n \nEfectos de sonido\n \nMusica")
        contr.escala=.5
        contr.x=-120
        contr.y=-50
        
        Grl = pilas.interfaz.Deslizador(75,-10)
        Efx = pilas.interfaz.Deslizador(75,-50)
        Mus = pilas.interfaz.Deslizador(75,-90)
        
        BtnGuardar = pilas.interfaz.Boton("Guardar", 50, -200)
        
        BtnVolver = pilas.interfaz.Boton("Volver", -50, -200)
            
        def volver():
            pilas.escenas.Config()
            
        BtnVolver.conectar(volver)
                  
        titulo = pilas.actores.Actor()
        titulo.imagen = "Imagenes\Titulo.png"
        titulo.escala=.6
        titulo.y=60
        
        
#-------------------Vinculacion de escenas------------------------
        
pilas.escenas.vincular(MenuInicial)
pilas.escenas.vincular(MenuPersonajes)
pilas.escenas.vincular(CombatArena)
pilas.escenas.vincular(Instrucciones)
pilas.escenas.vincular(Config)
pilas.escenas.vincular(Audio)
pilas.escenas.vincular(ControlesP1)
pilas.escenas.vincular(ControlesP2)

pilas.escenas.Audio()

pilas.ejecutar()