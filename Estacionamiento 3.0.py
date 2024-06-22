# Lista de tarifas del estacionamiento [horas, tarifa]
tarifas = [
    [1, 2000],
    [3, 5000],
    [5, 8000]
]

# Listas paralelas para almacenar información de clientes
dnis = []
facturacion_x_cliente = []
ingresos_x_cliente = []

# Función para mostrar las tarifas del estacionamiento
def mostrar_tarifas():
    print("Tarifas del estacionamiento:")
    for tarifa in tarifas:
        horas = tarifa[0]
        precio = tarifa[1]
        print(f"{horas} horas -> ${precio}")

# Función para buscar un cliente por su DNI en la lista
def buscar_cliente_secuencial(dni):
    indice_cliente = -1  # Valor por defecto si no se encuentra el cliente
    for i in range(len(dnis)):
        if dnis[i] == dni:
            indice_cliente = i  # Actualiza el índice si el cliente se encuentra
            break
    return indice_cliente

# Función para registrar el ingreso de un cliente
def registrar_ingreso():
    # Solicitar DNI hasta que se ingrese uno válido
    dni = ""
    while dni == "":
        dni = input("Ingrese su DNI: ")
        if dni == "":
            print("DNI no válido. Por favor, ingrese un DNI válido.")

    # Mostrar las tarifas del estacionamiento
    mostrar_tarifas()

    horas_input = ""
    while horas_input == "":
        # Solicitar la cantidad de horas hasta que se ingrese una válida o 'm' para volver al menú
        horas_input = input("Ingrese la cantidad de horas que pasará en el estacionamiento o 'm' para volver al menú: ")
        if horas_input.lower() == 'm':
            return
        # Verificar si la entrada es un número
        if not horas_input.isdigit():
            print("Entrada no válida. Por favor, ingrese un número de horas o 'm' para volver al menú.")
            horas_input = ""
            continue

        horas = int(horas_input)
        tarifa_elegida = None
        # Buscar la tarifa correspondiente a la cantidad de horas ingresada
        for tarifa in tarifas:
            if horas == tarifa[0]:
                tarifa_elegida = tarifa
        if tarifa_elegida is None:
            print("Cantidad de horas no válida.")
            horas_input = ""

    # Actualizar las listas de clientes
    index = buscar_cliente_secuencial(dni)
    if index != -1:
        # Si el cliente ya existe, actualizar sus ingresos y facturación
        ingresos_x_cliente[index] += 1
        facturacion_x_cliente[index] += tarifa_elegida[1]
    else:
        # Si el cliente no existe, agregarlo a las listas
        dnis.append(dni)
        ingresos_x_cliente.append(1)
        facturacion_x_cliente.append(tarifa_elegida[1])

# Función para mostrar la facturación total y la cantidad de clientes distintos
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

# Función para mostrar la facturación ordenada de mayor a menor por cliente
def mostrar_facturacion_ordenada():
    lista_dnis = len(dnis)
    # Ordenar las listas de acuerdo a la facturación de mayor a menor
    for i in range(lista_dnis):
        for j in range(0, lista_dnis-i-1):
            if facturacion_x_cliente[j] < facturacion_x_cliente[j+1]:
                # Intercambiar los elementos para ordenar
                facturacion_x_cliente[j], facturacion_x_cliente[j+1] = facturacion_x_cliente[j+1], facturacion_x_cliente[j]
                dnis[j], dnis[j+1] = dnis[j+1], dnis[j]

    print("Facturación por cliente de mayor a menor:")
    for i in range(lista_dnis):
        print(f"DNI: {dnis[i]}, Facturación: ${facturacion_x_cliente[i]}")

# Función para buscar el cliente que más veces ingresó al estacionamiento
def buscar_cliente_mas_ingresado():
    indice_max = -1  # Valor por defecto si no hay clientes registrados

    if ingresos_x_cliente:
        max_ingresos = ingresos_x_cliente[0]
        indice_max = 0

        for i in range(1, len(ingresos_x_cliente)):
            if ingresos_x_cliente[i] > max_ingresos:
                max_ingresos = ingresos_x_cliente[i]
                indice_max = i

    return indice_max

# Función para mostrar el cliente que más veces ingresó y su facturación total
def mostrar_cliente_mas_ingresado():
    indice = buscar_cliente_mas_ingresado()

    if indice == -1:
        print("No hay clientes registrados.")
    else:
        dni = dnis[indice]
        ingresos = ingresos_x_cliente[indice]
        facturacion = facturacion_x_cliente[indice]
        print(f"Cliente que más veces ingresó: DNI {dni}, Ingresos: {ingresos}, Facturación total: ${facturacion}")

# Función principal que maneja el menú y las opciones del programa
def main():
    salir = False
    while not salir:
        print("\nOpciones:")
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

# Ejecutar la función principal
main()
