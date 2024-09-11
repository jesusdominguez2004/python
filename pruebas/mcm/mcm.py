# Python MCM (Mínimo Común Múltiplo)

# 1. Leer números usuario
numero01 = int(input("Ingrese un primer número: "))
numero02 = int(input("Ingrese un segundo número: "))
cantidad_multiplos = int(input("Ingrese cantidad de múltiplos de consulta: "))

# 2. Obtener multiplos del usuario
numero01_multiplos = []
numero02_multiplos = []

for x in range(cantidad_multiplos):
    numero01_multiplo = numero01 * (x + 1)
    numero02_multiplo = numero02 * (x + 1)
    numero01_multiplos.append(numero01_multiplo)
    numero02_multiplos.append(numero02_multiplo)

# 3. Encontrar multiplos comunes
multiplos_comunes = []
for multiplo in numero01_multiplos:
    if multiplo in numero02_multiplos:
        multiplos_comunes.append(multiplo)

# 4. Calcular el menor múltiplo común
mcm = min(multiplos_comunes)

# 5. Mostrar resultados en consola
print(f"\nCantidad múltiplos: {cantidad_multiplos}")
print(f"Multiplos de {numero01}: {numero01_multiplos}")
print(f"Multiplos de {numero02}: {numero02_multiplos}")
print(f"Multiplos comunes: {multiplos_comunes}")
print(f"MCM: {mcm}")
