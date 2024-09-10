print("Mas sobre funciones")
# Aqui se escriben las funciones

def suma_ab(a,b):
    s1=a+b
    return s1
def resta_ab(c,d):
    s2=c-d
    return s2
def multiplicacion_ab(e,f):
    s3=e*f
    return s3
def div_ab(g,h):
    s4=g/h
    return s4

#Llmadas a funciones

print("Calculando suma")
n1=int(input("Ingresa el primer numero de suma "))
n2=int(input("Ingresa el segundo numero de suma "))
suma=suma_ab(n1,n2)
print(f"La suma de {n1} + {n2} es: {suma}")

print("-------------------------")

print("Calculando resta")
n3=int(input("Ingresa el primer numero de resta "))
n4=int(input("Ingresa el segundo numero de resta "))
resta=resta_ab(n3,n4)
print(f"La resta de {n3} - {n4} es: {resta}")

print("-------------------------")

print("Calculando Multiplicacion")
n5=int(input("Ingresa el primer numero de multiplicacion "))
n6=int(input("Ingresa el segundo numero de multiplicacion "))
multi=multiplicacion_ab(n5,n6)
print(f"La Multiplicacion de {n5} * {n6} es: {multi}")

print("-------------------------")

print("Calculando Divicion")
n7=int(input("Ingresa el primer numero de divicion "))
n8=int(input("Ingresa el segundo numero de divicion "))
div=div_ab(n7,n8)
print(f"La Divicion de {n7} / {n2} es: {div}")
