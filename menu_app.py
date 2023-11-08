def agregar_compra(compras, total_gastado):
    monto = float(input("Ingrese el monto de la compra: "))
    compras.append(monto)
    total_gastado += monto
    print(f"Compra de ${monto} agregada correctamente.")
    return total_gastado


def mostrar_compras(compras):
    if not compras:
        print("No hay compras registradas.")
    else:
        print("Lista de compras:")
        for i, compra in enumerate(compras, 1):
            print(f"Compra {i}: ${compra}")


def mostrar_total(total_gastado):
    print(f"Total gastado: ${total_gastado:.2f}")


def main():
    compras = []
    total_gastado = 0

    while True:
        print("\nMenú Principal:")
        print("1. Agregar compra")
        print("2. Mostrar compras")
        print("3. Mostrar total gastado")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            total_gastado = agregar_compra(compras, total_gastado)
        elif opcion == "2":
            mostrar_compras(compras)
        elif opcion == "3":
            mostrar_total(total_gastado)
        elif opcion == "4":
            print("¡Gracias por ocupar nuestro servicio, hasta pronto!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


if __name__ == "__main__":
    main()

