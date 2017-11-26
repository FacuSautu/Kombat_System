# coding: utf-8
import pilasengine

pilas = pilasengine.iniciar()

class Player2(pilasengine.actores.Actor):

    def iniciar(self, enemigoP1):
        global EnemyP1
        EnemyP1 = enemigoP1
        self.x = 200
        self.y = -150
        self.escala = .7
        self.espejado = True
        self.hacer_inmediatamente(ParadoP2)
        self.sombra = self.pilas.actores.Sombra()
        self.altura_del_salto = 0
        
        #Colision de el cuerpo
        global ColiderBodyP2
        ColiderBodyP2 = pilas.actores.Actor()
        ColiderBodyP2.transparencia = 100
        ColiderBodyP2.figura_de_colision = pilas.fisica.Rectangulo(0, 0, 100, 130)
        
        #Colision del golpe
        global ColiderHitP2
        ColiderHitP2 = pilas.actores.Actor()
        ColiderHitP2.transparencia = 100
        ColiderHitP2.figura_de_colision = None
        
        #Vida y energia del Jugador 2
        global VidaP2
        VidaP2 = pilas.actores.Energia(progreso=100, ancho=300, alto=25, x=165, y=220, color_relleno=colores.verde)
        VidaP2.espejado = True
        global EnergiaP1
        EnergiaP1 = pilas.actores.Energia(progreso=0, ancho=150, alto=25, x=-240, y=190)
        
        teclasP2 = {
            pilas.simbolos.IZQUIERDA: 'izquierda',
            pilas.simbolos.DERECHA: 'derecha',
            pilas.simbolos.ARRIBA: 'arriba',
            pilas.simbolos.k: 'abajo',
            pilas.simbolos.j: 'boton',
        }
        
        global mi_controlP2
        mi_controlP2 = pilas.control.Control(teclasP2)
        self.control = mi_controlP2
        
    def actualizar(self):
        self.sombra.x = self.x
        self.sombra.z = self.z + 1
        self.sombra.rotacion = self.rotacion
        
        ColiderBodyP2.x = self.x
        ColiderBodyP2.y = self.y + 80
        
        # Adapta el tamaño y la distancia a la sombra para simular
        # que la sombra está siempre 'pegada' al suelo del escenario.
        self.sombra.y = self.y + 20 - self.altura_del_salto
        self.sombra.escala = self.escala - self.altura_del_salto / 300.0
            
        def golpeadoP2():
            if not self.control.abajo:
                self.hacer_inmediatamente(AtackedP2)
            
        pilas.colisiones.agregar(ColiderBodyP2, EnemyP1, golpeadoP2)

class ParadoP2(pilasengine.comportamientos.Comportamiento):

    def iniciar(self, receptor):
        self.receptor = receptor
        self.control = mi_controlP2

        self.receptor.imagen = self.pilas.imagenes.cargar_grilla("Player2/P2Idle/FighterIdle8.png", 8, 1)
        self.receptor.centro = ("centro", "abajo")

    def actualizar(self):
        self.receptor.imagen.avanzar(10)
        
        # Si pulsa a los costados comienza a caminar.
        if self.control.derecha or self.control.izquierda:
            self.receptor.hacer_inmediatamente(CaminarP2)
            
        # Si pulsa hacia arriba salta.
        if self.control.arriba:
            self.receptor.hacer_inmediatamente(JumpP2)
            
         # Si pulsa el boton ataca.
        if self.control.boton:
            self.receptor.hacer_inmediatamente(AtackP2)
        # Si pulsa hacia abajo blockea    
        if self.control.abajo:
            self.receptor.hacer_inmediatamente(BlockP2)

class CaminarP2(pilasengine.comportamientos.Comportamiento):
    
    def iniciar(self, receptor):
        self.receptor = receptor
        self.control = mi_controlP2

        self.moveR = self.pilas.imagenes.cargar_grilla("Player2/P2Move/FighterRight8.png", 8, 1)
        self.moveL = self.pilas.imagenes.cargar_grilla("Player2/P2Move/FighterLeft8.png", 8, 1)
        
    def actualizar(self):
        self.receptor.imagen.avanzar(10)
        
        # Si pulsa a los costados se puede mover.
        if self.control.derecha:
            self.receptor.imagen = self.moveR
            self.receptor.centro = ("centro", "abajo")
            self.receptor.x += 2
        elif self.control.izquierda:
            self.receptor.imagen = self.moveL
            self.receptor.centro = ("centro", "abajo")
            self.receptor.x -= 2
            
        # Si pulsa hacia arriba salta.
        if self.control.arriba:
            self.receptor.hacer_inmediatamente(JumpP2)
            
        # Si suelta las teclas regresa al estado inicial.
        if not self.control.derecha and not self.control.izquierda:
            self.receptor.hacer_inmediatamente(ParadoP2)
            
        # Si pulsa el boton ataca.
        if self.control.boton:
            self.receptor.hacer_inmediatamente(AtackP2)
            
        # Si pulsa hacia abajo blockea    
        if self.control.abajo:
            self.receptor.hacer_inmediatamente(BlockP2)
            
class BlockP2(pilasengine.comportamientos.Comportamiento):
    def iniciar(self, receptor):
        self.receptor = receptor
        self.control = mi_controlP2
        
        self.receptor.imagen = self.pilas.imagenes.cargar_grilla("Player2/P2Block/FighterBlock6.png", 6, 1)
        self.receptor.centro = ("centro", "abajo")
        
        self.receptor.y -= 20
        
    def actualizar(self):
        self.receptor.imagen.avanzar(10)
        
        if not self.control.abajo:
            self.receptor.y += 20
            self.receptor.hacer_inmediatamente(ParadoP2)
            
class AtackedP2(pilasengine.comportamientos.Comportamiento):
    
    def iniciar(self, receptor):
        self.receptor = receptor
        self.control = mi_controlP2
        
        self.receptor.imagen = self.pilas.imagenes.cargar_grilla("Player2/P2Atacked/FighterAtacked10.png", 10, 1)
        self.receptor.centro = ("centro", "abajo")
        
        VidaP2.progreso -= 2
        EnergiaP1.progreso += 8
        
        def recuperadoP2():
            self.receptor.hacer_inmediatamente(ParadoP2)
            
        pilas.tareas.agregar(.2, recuperadoP2)
        
    def actualizar(self):
        self.receptor.imagen.avanzar(18)

class AtackP2(pilasengine.comportamientos.Comportamiento):
    
    def iniciar(self, receptor):
        self.receptor = receptor
        self.control = mi_controlP2
        
        self.receptor.imagen = self.pilas.imagenes.cargar_grilla("Player2/P2Atack/FighterAtack8.png", 8, 1)
        self.receptor.centro = ("centro", "abajo")
        
        ColiderHitP2.x = self.receptor.x - 50
        ColiderHitP2.y = self.receptor.y + 100
        ColiderHitP2.figura_de_colision = pilas.fisica.Circulo(radio = 10, sensor = True)
        
        def Timer():
            self.receptor.hacer_inmediatamente(ParadoP2)
            ColiderHitP2.figura_de_colision = None
        
        global TGolpeP2 
        TGolpeP2 = pilas.tareas.agregar(.5, Timer)
        
    def actualizar(self):
        self.receptor.imagen.avanzar(15)
        
         # Si pulsa hacia arriba salta.
        if self.control.arriba and not self.control.derecha and not self.control.izquierda:
            TGolpeP2.terminar()
            ColiderHitP2.figura_de_colision = None
            self.receptor.hacer_inmediatamente(JumpP2)
            
        # Si pulsa a los costados comienza a caminar.
        if self.control.derecha or self.control.izquierda and not self.control.arriba:
            TGolpeP2.terminar()
            ColiderHitP2.figura_de_colision = None
            self.receptor.hacer_inmediatamente(CaminarP2)
            
        # Si pulsa hacia abajo bloquea.
        if self.control.abajo:
            TGolpeP2.terminar()
            ColiderHitP2.figura_de_colision = None
            self.receptor.hacer_inmediatamente(BlockP2)
            
class JumpP2(pilasengine.comportamientos.Comportamiento):
    
    def iniciar(self, receptor):
        self.receptor = receptor
        self.control = mi_controlP2

        self.receptor.imagen = self.pilas.imagenes.cargar_grilla("Player2/P2Jump/FighterJump8.png", 8, 1)
        self.receptor.centro = ("centro", "abajo")
        self.y_inicial = self.receptor.y
        self.vy = 15
        
    def actualizar(self):
        self.receptor.imagen.avanzar(10)
        self.receptor.y += self.vy
        self.vy -= 0.7

        distancia_al_suelo = self.receptor.y - self.y_inicial
        self.receptor.altura_del_salto = distancia_al_suelo

        # Cuando llega al suelo, regresa al estado inicial.
        if distancia_al_suelo < 0:
            self.receptor.y = self.y_inicial
            self.receptor.altura_del_salto = 0
            self.receptor.hacer_inmediatamente(ParadoP2)
            
        # Si pulsa a los costados se puede mover.
        if self.control.derecha:
            self.receptor.x += 4
        elif self.control.izquierda:
            self.receptor.x -= 4
            

            
pilas.actores.vincular(Player2)

pilas.comportamientos.vincular(ParadoP2)
pilas.comportamientos.vincular(CaminarP2)
pilas.comportamientos.vincular(JumpP2)
pilas.comportamientos.vincular(AtackedP2)
pilas.comportamientos.vincular(AtackP2)
pilas.comportamientos.vincular(BlockP2)


Mono = pilas.actores.Mono(x= -200, y=-100)

P2 = pilas.actores.Player2(enemigoP1 = Mono)

pilas.ejecutar()