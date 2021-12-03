#Que retorne verdadero si el número ingresado es par,
# caso contrario falso

def number_is_even(number):
    return True if number%2 ==0 else False

#Que retorne verdadero si el número ingresado es impar,
# caso contrario falso

def number_is_add(number):
    return True if number %2 != 0 else False

#Que retorne los numeros pares de un intervalo

def list_even_number(number):
    list = []
    for i in range (number):
        list.append(i) if i %2 ==0 else None
    return list