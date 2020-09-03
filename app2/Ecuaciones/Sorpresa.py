import turtle

class Sorpresa:
    def __init__(self):
        super().__init__()

    def arbol(self,longitudRama,t):
        if longitudRama > 5:
            t.forward(longitudRama)
            t.right(20)
            arbol(longitudRama-15,t)
            t.left(40)
            arbol(longitudRama-15,t)
            t.right(20)
            t.backward(longitudRama)

    def main(self):
        t = turtle.Turtle()
        miVentana = turtle.Screen()
        t.left(90)
        t.up()
        t.backward(100)
        t.down()
        t.color("green")
        self.arbol(75,t)
        miVentana.exitonclick()

    def Ejecutar(self):
        self.main()
