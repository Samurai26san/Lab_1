# Lab_1

# 1. Suma de n números
n = int(input("¿Cuántos números quieres sumar? "))
nums = [int(input("Número: ")) for _ in range(n)]
print("Suma total:", sum(nums))

# 2. Invertir número
num = input("Ingrese un número para invertir: ")
print("Número invertido:", num[::-1])

# 3. Pedir nombre, edad y profesión
name = input("Nombre: ")
age = input("Edad: ")
profession = input("Profesión: ")
print(f"Hola {name}, tienes {age} años y eres {profession}.")

# 4. Números únicos
x = int(input("¿Cuántos números ingresarás? "))
numbers = [int(input("Número: ")) for _ in range(x)]
print("Valores únicos:", list(set(numbers)))
