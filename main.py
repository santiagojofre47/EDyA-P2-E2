from conversor_binario import Conversor

if __name__ == '__main__':
    x = 50
    conver = Conversor()
    conver.dividir_sucesivamente(x)
    print('Numero decimal {} convertido a binario: '.format(x))
    conver.mostrar_resultado()
            
        