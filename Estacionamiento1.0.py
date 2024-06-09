# Lista de tarifas del estacionamiento [horas, tarifa]
tarifas = [
    [1, 2000],
    [3, 5000],
    [5, 8000]
]

# Listas paralelas
dnis = []
facturacion_x_cliente = []
ingresos_x_cliente = []

def mostrar_tarifas():
    print("Tarifas del estacionamiento:")
    for tarifa in tarifas:
        horas = tarifa[0]
        precio = tarifa[1]
        print(f"{horas} horas -> ${precio}")

def buscar_cliente_secuencial(dni):
    for i in range(len(dnis)):
        if dnis[i] == dni:
            return i
    return -1

def registrar_ingreso():
    dni = ""
    while dni == "":
        dni = input("Ingrese su DNI: ")
        if dni == "":
            print("DNI no válido. Por favor, ingrese un DNI válido.")

    mostrar_tarifas()

    horas_input = ""
    while horas_input == "":
        horas_input = input("Ingrese la cantidad de horas que pasará en el estacionamiento o 'm' para volver al menú: ")
        if horas_input.lower() == 'm':
            return
        try:
            horas = int(horas_input)
            tarifa_elegida = None
            for tarifa in tarifas:
                if horas == tarifa[0]:
                    tarifa_elegida = tarifa
            if tarifa_elegida is None:
                print("Cantidad de horas no válida.")
                horas_input = ""
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número de horas o 'm' para volver al menú.")
            horas_input = ""

    # Actualizar las listas
    index = buscar_cliente_secuencial(dni)
    if index != -1:
        ingresos_x_cliente[index] += 1
        facturacion_x_cliente[index] += tarifa_elegida[1]
    else:
        dnis.append(dni)
        ingresos_x_cliente.append(1)
        facturacion_x_cliente.append(tarifa_elegida[1])

def mostrar_facturacion_total_y_clientes():
    total_facturacion = sum(facturacion_x_cliente)

    # Crear una lista única de DNIs sin duplicados
    clientes_distintos = []
    for dni in dnis:
        if dni not in clientes_distintos:
            clientes_distintos.append(dni)

    total_clientes = len(clientes_distintos)

    print(f"Facturación total del día: ${total_facturacion}")
    print(f"Cantidad de clientes distintos: {total_clientes}")

def mostrar_facturacion_ordenada():
    lista_dnis = len(dnis)
    # Ordenar las listas de acuerdo a la facturación de mayor a menor
    for i in range(lista_dnis):
        for j in range(0, lista_dnis-i-1):
            if facturacion_x_cliente[j] < facturacion_x_cliente[j+1]:
                facturacion_x_cliente[j], facturacion_x_cliente[j+1] = facturacion_x_cliente[j+1], facturacion_x_cliente[j]
                dnis[j], dnis[j+1] = dnis[j+1], dnis[j]

    print("Facturación por cliente de mayor a menor:")
    for i in range(lista_dnis):
        print(f"DNI: {dnis[i]}, Facturación: ${facturacion_x_cliente[i]}")

def buscar_cliente_mas_ingresado():
    if not ingresos_x_cliente:
        return -1

    max_ingresos = ingresos_x_cliente[0]
    indice_max = 0

    for i in range(1, len(ingresos_x_cliente)):
        if ingresos_x_cliente[i] > max_ingresos:
            max_ingresos = ingresos_x_cliente[i]
            indice_max = i

    return indice_max

def mostrar_cliente_mas_ingresado():
    indice = buscar_cliente_mas_ingresado()

    if indice == -1:
        print("No hay clientes registrados.")
        return

    dni = dnis[indice]
    ingresos = ingresos_x_cliente[indice]
    facturacion = facturacion_x_cliente[indice]
    print(f"Cliente que más veces ingresó: DNI {dni}, Ingresos: {ingresos}, Facturación total: ${facturacion}")

def main():
    salir = False
    while not salir:
        print("Opciones:")
        print("1. Registrar ingreso")
        print("2. Mostrar facturación total y cantidad de clientes distintos")
        print("3. Mostrar facturación ordenada de mayor a menor por cliente")
        print("4. Mostrar cliente que más veces ingresó y su facturación total")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            registrar_ingreso()
        elif opcion == '2':
            mostrar_facturacion_total_y_clientes()
        elif opcion == '3':
            mostrar_facturacion_ordenada()
        elif opcion == '4':
            mostrar_cliente_mas_ingresado()
        elif opcion == '5':
            salir = True
        else:
            print("Opción no válida. Intente nuevamente.")

main()
