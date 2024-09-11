# Python MCM (Mínimo Común Múltiplo)

# 1. Leer números usuario
numero01 = input("Ingrese un primer número: ")
numero02 = input("Ingrese un segundo número: ")
cantidad_multiplos = input("Ingrese cantidad de múltiplos de consulta: ")

if numero01.isdigit() and numero02.isdigit() and cantidad_multiplos.isdigit():
    numero01 = int(numero01)
    numero02 = int(numero02)
    cantidad_multiplos = int(cantidad_multiplos)

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
    if len(multiplos_comunes) > 0:
        mcm = min(multiplos_comunes)
    else:
        mcm = None
        multiplos_comunes = None
else:
    numero01 = None
    numero02 = None
    cantidad_multiplos = None
    numero01_multiplos = None
    numero02_multiplos = None
    multiplos_comunes = None
    mcm = None

# 5. Mostrar resultados en consola
print(f"\nCantidad múltiplos: {cantidad_multiplos}")
print(f"Multiplos de {numero01}: {numero01_multiplos}")
print(f"Multiplos de {numero02}: {numero02_multiplos}")
print(f"Multiplos comunes: {multiplos_comunes}")
print(f"MCM: {mcm}")
