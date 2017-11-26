# coding: utf-8
import pilasengine

#Se saco esto por problemas al importar
pilas = pilasengine.iniciar()

class Audio(pilasengine.escenas.Escena):
    def iniciar(self):
                       
#-------Preparando el Fondo---------------------------------------------------
    
        gFondo = pilas.imagenes.cargar_grilla('Imagenes\FondoMenu.png', 12)
        fondo = pilas.actores.Animacion(gFondo, ciclica=True, velocidad= 10)
        pilas.camara.escala=2.25
        fondo.z=-10
 
#-----------------------Subtitulo------------------------------------------------------------
         
        subtitulo = pilas.actores.Texto("Audio", y = 80)
        subtitulo.y = 80
                      
#--------------------Nombre de opciones------------------------------------------------
 
        contr = pilas.actores.Texto("General\n \nEfectos de sonido\n \nMusica")
        contr.escala=.5
        contr.x=-120
        contr.y=-50
 
#-----------------------------Configuracion de audio---------------------------------------
           
        Grl = pilas.interfaz.Deslizador(75,-10)
        Efx = pilas.interfaz.Deslizador(75,-50)
        Mus = pilas.interfaz.Deslizador(75,-90)

#-----------------------------Boton de guardado---------------------------------------
            
        BtnGuardar = pilas.interfaz.Boton("Guardar", 50, -200)
 
#-----------------------------Volver con escape---------------------------------------
                         
        def volver():
            pilas.escenas.Config()
         
#-----------------------------Titulo del juego---------------------------------------
              
        titulo = pilas.actores.Actor()
        titulo.imagen = "Imagenes\Titulo.png"
        titulo.escala=.6
        titulo.y=60
        
        
#-------------------Vinculacion de escenas------------------------
        
#pilas.escenas.vincular(MenuInicial)
#pilas.escenas.vincular(MenuPersonajes)
#pilas.escenas.vincular(CombatArena)
#pilas.escenas.vincular(Instrucciones)
#pilas.escenas.vincular(Config)
#pilas.escenas.vincular(Audio)
#pilas.escenas.vincular(ControlesP1)
#pilas.escenas.vincular(ControlesP2)

#pilas.escenas.Audio()

#pilas.ejecutar()