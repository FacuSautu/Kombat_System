# coding: utf-8
import pilasengine

pilas = pilasengine.iniciar()

class MenuPersonajes(pilasengine.escenas.Escena):
    def iniciar(self):
        
        
        gFondo = pilas.imagenes.cargar_grilla('Imagenes\FondoMenu.png', 12)
        fondo = pilas.actores.Animacion(gFondo, ciclica=True, velocidad= 10)
        pilas.camara.escala=2.25
        fondo.z=10
        
        PJFacu = pilas.actores.Actor(imagen = "Imagenes\Fighters\Facu.jpg", x=-60)
        PJFacu.escala = .1
        PJRami = pilas.actores.Actor(imagen="Imagenes\Fighters\Rami.jpg")
        PJRami.escala = .1
        PJNacho = pilas.actores.Actor(imagen="Imagenes\Fighters\Nacho.jpg", x=60)
        PJNacho.escala = .1
        PJFede = pilas.actores.Actor(imagen="Imagenes\Fighters\Fede.jpg", x=-60, y=-50)
        PJFede.escala = .1
        PJStefan = pilas.actores.Actor(imagen="Imagenes\Fighters\Stefan.jpg", y=-50)
        PJStefan.escala = .1
        PJLucas = pilas.actores.Actor(imagen="Imagenes\Fighters\Lucas.jpg", x=60, y=-50)
        PJLucas.escala = .1
    
        subtitulo = pilas.actores.Texto("Selecciones su personaje")
        subtitulo.y=80
     
        BtnSiguiente = pilas.interfaz.Boton("Fight!",0,-200)
                    
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

pilas.escenas.MenuPersonajes()

pilas.ejecutar()