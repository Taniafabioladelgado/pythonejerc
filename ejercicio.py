#  Escribir un programa que lea un entero positivo, n, introducido usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta n. La suma de los  primeros enteros positivos puede ser calculada de la siguiente forma: suma = n(n+1)/2

n = int(input("Introduce un número entero: "))
sum = (n*(n+1))/2
print(sum)

#Implementa un generador que produzca los números de la secuencia Fibonacci.

def fibonacci_gen():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
fib = fibonacci_gen()
for _ in range(10):
    print(next(fib))

#Ingresar dos numeros donde se entregue el numero mayor de estos.

a = int(input('ingrese un numero: '))
b = int(input('ingrese otro numero: '))

print(a,b)

if b>a:
    print("El numero ",b,"es mayor que ",a)

elif b<a:
    print("El numero",a,"es mayor que ",b)

else:
    print("Los numeros son iguales")