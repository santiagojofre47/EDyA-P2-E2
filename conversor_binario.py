import math
from clasePilaEncadenada import Pila

class Conversor(object):
    __pila = None
    
    def __init__(self):
        self.__pila = Pila()
    
    def dividir_sucesivamente(self, numero):
        assert isinstance(numero, int)
        while numero >= 1:
            aux = numero%2
            numero = math.floor(numero/2)
            self.__pila.insertar(aux)
    
    def mostrar_resultado(self):
        if not self.__pila.vacia():
            while self.__pila.getCantidad() > 0:
                print('{}'.format(self.__pila.suprimir()))