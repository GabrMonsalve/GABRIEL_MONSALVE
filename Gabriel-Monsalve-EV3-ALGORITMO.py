import numpy as np

asientos = np.array([
    ["A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A9", "A10", "A11", "A12", "A13", "A14", "A15"],
    ["B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9", "B10", "B11", "B12", "B13", "B14", "B15"],
    ["C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C10", "C11", "C12", "C13", "C14", "C15"],
    ["D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9", "D10", "D11", "D12", "D13", "D14", "D15"],
    ["E1", "E2", "E3", "E4", "E5", "E6", "E7", "E8", "E9", "E10", "E11", "E12", "E13", "E14", "E15"],
    ["F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10", "F11", "F12", "F13", "F14", "F15"]
])

cupos_asientos = np.count_nonzero(asientos != '')
cupos_cancha = 899

total_vendido_asientos = 0
total_vendido_cancha = 0
ticket_correlativo = 0

def mostrar_disponibilidad():
    print("Asientos disponibles:")
    for fila in asientos:
        print(" ".join([asiento if asiento else "--" for asiento in fila]))
    print("Cantidad de asientos disponibles:", cupos_asientos)
    print("Cantidad de cupos disponibles en cancha:", cupos_cancha)

def vender_entrada():
    global cupos_asientos, cupos_cancha, total_vendido_asientos, total_vendido_cancha, ticket_correlativo

    tipo_entrada = input("Seleccione el tipo de entrada a vender (A: Asiento, C: Cancha): ")
    tipo_entrada = tipo_entrada.upper()

    if tipo_entrada == 'A':
        fila_asiento = input("Ingrese el número de asiento a vender (por ejemplo, A1): ")
        if not fila_asiento:
            print("Debe ingresar un asiento válido.")
            return

        fila_asiento = fila_asiento.upper()
        fila_index = ord(fila_asiento[0]) - 65
        columna_index = int(fila_asiento[1:]) - 1

        if fila_index < 0 or fila_index >= len(asientos) or columna_index < 0 or columna_index >= len(asientos[fila_index]):
            print("Asiento inválido.")
            return

        if asientos[fila_index][columna_index]:
            asientos[fila_index][columna_index] = None
            cupos_asientos -= 1
            total_vendido_asientos += 1
            print("¡Entrada vendida correctamente!")
        else:
            print("El asiento ya está vendido.")
    elif tipo_entrada == 'C':
        nombre = input("Ingresa tu nombre: ")
        apellido = input("Ingresa tu apellido: ")

        if cupos_cancha <= 0:
            print("No hay suficientes cupos disponibles en la cancha.")
            return

        ticket_correlativo += 1
        cupos_cancha -= 1
        total_vendido_cancha += 1

        print("Ticket vendido correctamente. No hay devoluciones")
        print("Nombre:", nombre)
        print("Apellido:", apellido)
        print("Número de ticket:", ticket_correlativo)
    else:
        print("Tipo de entrada inválido.")

def mostrar_total_vendido():
    total_vendido_asientos_valor = total_vendido_asientos * 10000
    total_vendido_cancha_valor = total_vendido_cancha * 5000

    print("Total de entradas vendidas:")
    print("Se han vendido", total_vendido_cancha, "entradas de cancha.")
    print("Por un valor de $5.000 cada una.")
    print("Total Vendido: $" + str(total_vendido_cancha_valor))
    print()
    print("Se han vendido", total_vendido_asientos, "asientos.")
    print("Por un valor de $10.000 cada uno.")
    print("Total Vendido: $" + str(total_vendido_asientos_valor))
    print()
    print("Total Vendido (asientos + cancha): $" + str(total_vendido_asientos_valor + total_vendido_cancha_valor))

def ver_disponibles():
    print("Asientos disponibles:")
    for fila in asientos:
        print(" ".join([asiento if asiento else "--" for asiento in fila]))

ver_disponibles()

# Ejecución del programa
while True:
    print("----- Menú -----")
    print("1. Mostrar disponibilidad de asientos")
    print("2. Vender entrada")
    print("3. Mostrar total de entradas vendidas")
    print("4. Ver asientos disponibles")
    print("5. Salir")

    opcion = input("Ingrese una opción: ")
    if opcion == '1':
        mostrar_disponibilidad()
    elif opcion == '2':
        vender_entrada()
    elif opcion == '3':
        mostrar_total_vendido()
    elif opcion == '4':
        ver_disponibles()
    elif opcion == '5':
        print("¡Aqui Organizamos agradece su preferencia!")
        break
    else:
        print("Opción inválida. Intente nuevamente.")
