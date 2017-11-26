# coding: utf-8
import pilasengine

#Se saco esto por problemas al importar
pilas = pilasengine.iniciar()

class ControlesP1(pilasengine.escenas.Escena):
    def iniciar(self):
                
#-------Preparando el Fondo---------------------------------------------------
                
        gFondo = pilas.imagenes.cargar_grilla('Imagenes\FondoMenu.png', 12)
        fondo = pilas.actores.Animacion(gFondo, ciclica=True, velocidad= 10)
        pilas.camara.escala=2.25
        fondo.z=-10

#-----------------------Subtitulo------------------------------------------------------------
                                        
        subtitulo = pilas.actores.Texto("Controles Player 1")
        subtitulo.y=80
                
#--------------------Nombre de opciones------------------------------------------------
 
        contr = pilas.actores.Texto("Saltar\n \nIzquierda\n \nDerecha\n \nGolpear\n \nBloquear\n \nHabilidad Especial")
        contr.escala=.5
        contr.x=-120
        contr.y=-50

#-----------------------------Definicion de teclas---------------------------------------
           
        Saltar = pilas.interfaz.IngresoDeTexto("Arriba",120,46,100,15)
        Izquierda = pilas.interfaz.IngresoDeTexto("Izquierda",120,6,100,15)
        Derecha = pilas.interfaz.IngresoDeTexto("Derecha",120,-36,100,15)
        Golpear = pilas.interfaz.IngresoDeTexto("J",120,-76,100,15)
        Bloquear = pilas.interfaz.IngresoDeTexto("K",120,-116,100,15)
        HabEspecial = pilas.interfaz.IngresoDeTexto("L",120,-156,100,15)

#--------------------------Boton de guardado---------------------------------------------
          
        BtnGuardar = pilas.interfaz.Boton("Guardar",0,-200)

#--------------------------Guardado de configuracion------------------------------------
           
        def guardar_cont_P1(self,saltar,izquierda,derecha,golpear,bloquear,habEspecial):
            saltar = Saltar.Texto
            izquierda = Izquierda.Texto
            derecha = Derecha.Texto
            golpear = Golpear.Texto
            bloquear = Bloquear.Texto
            habEspecial = HabEspecial.Texto
              
#---------------------------Titulo del juego--------------------------------------------------            
                        
        titulo = pilas.actores.Actor()
        titulo.imagen = "Imagenes\Titulo.png"
        titulo.escala=.6
        titulo.y=60
        
#-------------------Vinculacion de escenas----------------------------------------------
        
#pilas.escenas.vincular(MenuInicial)
#pilas.escenas.vincular(MenuPersonajes)
#pilas.escenas.vincular(CombatArena)
#pilas.escenas.vincular(Instrucciones)
#pilas.escenas.vincular(Config)
#pilas.escenas.vincular(Audio)
#pilas.escenas.vincular(ControlesP1)
#pilas.escenas.vincular(ControlesP2)

#pilas.escenas.ControlesP1()

#pilas.ejecutar()