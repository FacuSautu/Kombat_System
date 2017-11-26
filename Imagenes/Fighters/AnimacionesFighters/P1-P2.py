# coding: utf-8
import pilasengine

pilas = pilasengine.iniciar()

class Player1(pilasengine.actores.Actor):

    def iniciar(self):
        self.x = -200
        self.y = -150
        self.escala = .7
        self.hacer_inmediatamente(ParadoP1)
        self.sombra = self.pilas.actores.Sombra()
        self.altura_del_salto = 0
        
    def actualizar(self):
        self.sombra.x = self.x
        self.sombra.z = self.z + 1
        self.sombra.rotacion = self.rotacion
        
        # Adapta el tamaño y la distancia a la sombra para simular
        # que la sombra está siempre 'pegada' al suelo del escenario.
        self.sombra.y = self.y + 20 - self.altura_del_salto
        self.sombra.escala = self.escala - self.altura_del_salto / 300.0

class ParadoP1(pilasengine.comportamientos.Comportamiento):

    def iniciar(self, receptor):
        
        self.receptor = receptor
        self.control = receptor.pilas.control

        self.receptor.imagen = self.pilas.imagenes.cargar_grilla("Player1/P1Idle/FighterIdle.png", 10, 1)
        self.receptor.centro = ("centro", "abajo")

    def actualizar(self):
        self.receptor.imagen.avanzar(10)
        
        # Si pulsa a los costados comienza a caminar.
        if self.control.derecha or self.control.izquierda:
            self.receptor.hacer_inmediatamente(CaminarP1)
            
        # Si pulsa hacia arriba salta.
        if self.control.arriba:
            self.receptor.hacer_inmediatamente(JumpP1)
            
         # Si pulsa el boton ataca.
        if self.control.boton:
            self.receptor.hacer_inmediatamente(AtackP1)
            
        # Si pulsa hacia abajo bloquea.
        if self.control.abajo:
            self.receptor.hacer_inmediatamente(BlockP1)

class CaminarP1(pilasengine.comportamientos.Comportamiento):
    
    def iniciar(self, receptor):
        self.receptor = receptor
        self.control = receptor.pilas.control

        self.moveL = self.pilas.imagenes.cargar_grilla("Player1/P1Move/FighterLeft.png", 11, 1)
        self.moveR = self.pilas.imagenes.cargar_grilla("Player1/P1Move/FighterRight.png", 11, 1)
        
    def actualizar(self):
        self.receptor.imagen.avanzar(10)
        
        # Si pulsa a los costados se puede mover.
        if self.control.derecha:
            self.receptor.imagen = self.moveR
            self.receptor.centro = ("centro", "abajo")
            self.receptor.x += 3
        elif self.control.izquierda:
            self.receptor.imagen = self.moveL
            self.receptor.centro = ("centro", "abajo")
            self.receptor.x -= 3
            
        # Si pulsa hacia arriba salta.
        if self.control.arriba:
            self.receptor.hacer_inmediatamente(JumpP1)
            
        # Si suelta las teclas regresa al estado inicial.
        if not self.control.derecha and not self.control.izquierda:
            self.receptor.hacer_inmediatamente(ParadoP1)
            
        # Si pulsa el boton ataca.
        if self.control.boton:
            self.receptor.hacer_inmediatamente(AtackP1)
            
        # Si pulsa hacia abajo bloquea.
        if self.control.abajo:
            self.receptor.hacer_inmediatamente(BlockP1)
            
class BlockP1(pilasengine.comportamientos.Comportamiento):
    def iniciar(self, receptor):
        self.receptor = receptor
        self.control = receptor.pilas.control
        
        self.receptor.imagen = self.pilas.imagenes.cargar_grilla("Player1/P1Block/FighterBlocking.png", 5, 1)
        self.receptor.centro = ("centro", "abajo")
          
    def actualizar(self):
        self.receptor.imagen.avanzar(10)
        
        if not self.control.abajo:
            self.receptor.hacer_inmediatamente(ParadoP1)
            
class AtackP1(pilasengine.comportamientos.Comportamiento):
    
    def iniciar(self, receptor):
        self.receptor = receptor
        self.control = receptor.pilas.control
        
        self.receptor.imagen = self.pilas.imagenes.cargar_grilla("Player1/P1Atack/FighterAtack.png", 12, 1)
        self.receptor.centro = ("centro", "abajo")
         
        global ColiderP1
        ColiderP1 = pilas.actores.Actor()
        ColiderP1.imagen = "colision.png"
        ColiderP1.transparencia = 100
        ColiderP1.x = self.receptor.x + 60
        ColiderP1.y = self.receptor.y +100
        
        #Tarea para que la animacion dure todo un golpe
        # y que la colision del golpe desaparesca 
        def Timer():
            self.receptor.hacer_inmediatamente(ParadoP1)
            ColiderP1.eliminar()
        
        global TGolpe 
        TGolpe = pilas.tareas.agregar(.5, Timer)
        
    def actualizar(self):
        self.receptor.imagen.avanzar(20)
        
         # Si pulsa hacia arriba salta.
        if self.control.arriba:
            self.receptor.hacer_inmediatamente(JumpP1)
            TGolpe.terminar()
            ColiderP1.eliminar()
            
            
        # Si pulsa a los costados comienza a caminar.
        if self.control.derecha or self.control.izquierda and not self.control.boton and not self.control.arriba:
            self.receptor.hacer_inmediatamente(CaminarP1)
            TGolpe.terminar()
            ColiderP1.eliminar()
            
        # Si pulsa hacia abajo bloquea.
        if self.control.abajo:
            self.receptor.hacer_inmediatamente(BlockP1)
            TGolpe.terminar()
            ColiderP1.eliminar()
            
            
class JumpP1(pilasengine.comportamientos.Comportamiento):
    
    def iniciar(self, receptor):
        self.receptor = receptor
        self.control = receptor.pilas.control

        self.receptor.imagen = self.pilas.imagenes.cargar_grilla("Player1/P1Jump/FighterJump.png", 10, 1)
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
            self.receptor.hacer_inmediatamente(ParadoP1)
            
        # Si pulsa a los costados se puede mover.
        if self.control.derecha:
            self.receptor.x += 4
        elif self.control.izquierda:
            self.receptor.x -= 4
            
            
            
            
            
            
            
class Player2(pilasengine.actores.Actor):

    def iniciar(self):
        self.x = 200
        self.y = -150
        self.escala = .7
        self.espejado = True
        self.hacer_inmediatamente(ParadoP2)
        self.sombra = self.pilas.actores.Sombra()
        self.altura_del_salto = 0
        
    def actualizar(self):
        self.sombra.x = self.x
        self.sombra.z = self.z + 1
        self.sombra.rotacion = self.rotacion
        
        # Adapta el tamaño y la distancia a la sombra para simular
        # que la sombra está siempre 'pegada' al suelo del escenario.
        self.sombra.y = self.y + 20 - self.altura_del_salto
        self.sombra.escala = self.escala - self.altura_del_salto / 300.0

class ParadoP2(pilasengine.comportamientos.Comportamiento):

    def iniciar(self, receptor):
        self.receptor = receptor
        self.control = receptor.pilas.control

        self.receptor.imagen = self.pilas.imagenes.cargar_grilla("Player2/P2Idle/FighterIdle.png", 8, 1)
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
        self.control = receptor.pilas.control

        self.moveR = self.pilas.imagenes.cargar_grilla("Player2/P2Move/FighterRight.png", 8, 1)
        self.moveL = self.pilas.imagenes.cargar_grilla("Player2/P2Move/FighterLeft.png", 8, 1)
        
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
        self.control = receptor.pilas.control
        
        self.receptor.imagen = self.pilas.imagenes.cargar_grilla("Player2/P2Block/FighterBlock.png", 6, 1)
        self.receptor.centro = ("centro", "abajo")
        self.receptor.y = self.receptor.y - 30
        
    def actualizar(self):
        self.receptor.imagen.avanzar(10)
        
        if not self.control.abajo:
            self.receptor.hacer_inmediatamente(ParadoP2)
            self.receptor.y = self.receptor.y + 30
            
class AtackP2(pilasengine.comportamientos.Comportamiento):
    
    def iniciar(self, receptor):
        self.receptor = receptor
        self.control = receptor.pilas.control
        
        self.receptor.imagen = self.pilas.imagenes.cargar_grilla("Player2/P2Atack/FighterAtack.png", 8, 1)
        self.receptor.centro = ("centro", "abajo")
        
        global ColiderP2
        ColiderP2 = pilas.actores.Actor()
        ColiderP2.imagen = "colision.png"
        ColiderP2.transparencia = 100
        ColiderP2.x = self.receptor.x - 60
        ColiderP2.y = self.receptor.y + 100
        
        def Timer():
            self.receptor.hacer_inmediatamente(ParadoP2)
            ColiderP2.eliminar()
        
        global TGolpe 
        TGolpe = pilas.tareas.agregar(.7, Timer)
        
    def actualizar(self):
        self.receptor.imagen.avanzar(13)
        
         # Si pulsa hacia arriba salta.
        if self.control.arriba:
            self.receptor.hacer_inmediatamente(JumpP2)
            TGolpe.terminar()
            ColiderP2.eliminar()
            
        # Si pulsa a los costados comienza a caminar.
        if self.control.derecha or self.control.izquierda and not self.control.boton and not self.control.arriba:
            self.receptor.hacer_inmediatamente(CaminarP2)
            TGolpe.terminar()
            ColiderP2.eliminar()
        
        if self.control.abajo:
            self.receptor.hacer_inmediatamente(BlockP2)
            TGolpe.terminar()
            ColiderP2.eliminar()
            
class JumpP2(pilasengine.comportamientos.Comportamiento):
    
    def iniciar(self, receptor):
        self.receptor = receptor
        self.control = receptor.pilas.control

        self.receptor.imagen = self.pilas.imagenes.cargar_grilla("Player2/P2Jump/FighterJump.png", 8, 1)
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
            
pilas.actores.vincular(Player1)
pilas.actores.vincular(Player2)

pilas.comportamientos.vincular(ParadoP1)
pilas.comportamientos.vincular(CaminarP1)
pilas.comportamientos.vincular(JumpP1)
pilas.comportamientos.vincular(BlockP1)

pilas.comportamientos.vincular(ParadoP2)
pilas.comportamientos.vincular(CaminarP2)
pilas.comportamientos.vincular(JumpP2)
pilas.comportamientos.vincular(AtackP2)
pilas.comportamientos.vincular(BlockP2)

P2 = pilas.actores.Player2()
P1 = pilas.actores.Player1()

pilas.ejecutar()