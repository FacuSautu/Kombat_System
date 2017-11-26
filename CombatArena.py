# coding: utf-8
import pilasengine

#Se saco esto por problemas al importar
pilas = pilasengine.iniciar()

class CombatArena(pilasengine.escenas.Escena):
    def iniciar(self):
        
#-----------------------------Preparando el fondo---------------------------------------
    
        cFondo = pilas.imagenes.cargar_grilla('Imagenes\CombatArena3.png', 4)
        fondo = pilas.actores.Animacion(cFondo, ciclica=True, velocidad= 10)
        pilas.camara.escala=1.35
        fondo.z=10

#-----------------------------Interfaz de vida/energia---------------------------------------
            
        VidaP1 = pilas.actores.Energia(progreso=100, ancho=300, alto=25, x=-165, y=220, color_relleno=colores.verde)
        VidaP2 = pilas.actores.Energia(progreso=100, ancho=300, alto=25, x=165, y=220, color_relleno=colores.verde)
        VidaP2.espejado = True
        EnergiaP1 = pilas.actores.Energia(progreso=100, ancho=150, alto=25, x=-240, y=190)
        EnergiaP2 = pilas.actores.Energia(progreso=100, ancho=150, alto=25, x=240, y=190)  
        EnergiaP2.espejado = True

#-----------------------------Iniciando jugador/es---------------------------------------
            
    def cargar_jugadores1(self, pj1):
        PlayerIdleG = pilas.imagenes.cargar_grilla("Imagenes\Fighters\Player1.png", 315,45)
        PlayerIdleA = pilas.actores.Animacion(PlayerIdleG, ciclica=True, velocidad=10)
        PlayerIdleA.z=10
        PlayeridleA.escala=.5
        Player1= pilas.actores.Acto
              
#-------------------Vinculacion de escenas------------------------
        
#pilas.escenas.vincular(MenuInicial)
#pilas.escenas.vincular(MenuPersonajes)
#pilas.escenas.vincular(CombatArena)
#pilas.escenas.vincular(Instrucciones)
#pilas.escenas.vincular(Config)
#pilas.escenas.vincular(Audio)
#pilas.escenas.vincular(ControlesP1)
#pilas.escenas.vincular(ControlesP2)

#pilas.escenas.CombatArena()

#pilas.ejecutar()