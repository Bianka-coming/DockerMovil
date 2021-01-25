def calcular_factorial (x : int) :
    if(x <= 1):
        resultado = 1
    else :
        resultado = x * calcular_factorial(x-1)
    return resultado

if __name__ == '__main__':
    print("El factorial de 6 es : " , calcular_factorial(6))


