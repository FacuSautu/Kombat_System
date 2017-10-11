import pilasengine

class Fede(pilasengine.actores.Actor):
    def iniciar(self):
        self.imagen = "Rami.png"
        self.x = 0
        self.y = 0
    def actualizar(self):
        if self.pilas.control.izquierdo:
            self.x -= -10
            self.espejado = True
        if self.pilas.control.derecho:
            self.x += 10
            self.espejado = False