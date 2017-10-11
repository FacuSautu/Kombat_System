# coding: utf-8
import pilasengine

pilas = pilasengine.iniciar()

class ControlesP2(pilasengine.escenas.Escena):
    def iniciar(self):
        gFondo = pilas.imagenes.cargar_grilla('Imagenes\FondoMenu.png', 12)
        fondo = pilas.actores.Animacion(gFondo, ciclica=True, velocidad= 10)
        pilas.camara.escala=2.25
        fondo.z=-10
        
        subtitulo = pilas.actores.Texto("Controles Player 2")
        subtitulo.y=80
        contr = pilas.actores.Texto("Saltar\n \nIzquierda\n \nDerecha\n \nGolpear\n \nBloquear\n \nHabilidad Especial")
        contr.escala=.5
        contr.x=-120
        contr.y=-50
        
        Saltar = pilas.interfaz.IngresoDeTexto("W",120,46,100,15)
        Izquierda = pilas.interfaz.IngresoDeTexto("A",120,6,100,15)
        Derecha = pilas.interfaz.IngresoDeTexto("D",120,-36,100,15)
        Golpear = pilas.interfaz.IngresoDeTexto("F",120,-76,100,15)
        Bloquear = pilas.interfaz.IngresoDeTexto("G",120,-116,100,15)
        HabEspecial = pilas.interfaz.IngresoDeTexto("H",120,-156,100,15)
        
        BtnGuardar = pilas.interfaz.Boton("Guardar",0,-200)
        
        def guardar_cont_P2(self,saltar,izquierda,derecha,golpear,bloquear,habEspecial):
            saltar = Saltar.Texto
            izquierda = Izquierda.Texto
            derecha = Derecha.Texto
            golpear = Golpear.Texto
            bloquear = Bloquear.Texto
            habEspecial = HabEspecial.Texto
        
            
                    
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

pilas.escenas.ControlesP2()

pilas.ejecutar()