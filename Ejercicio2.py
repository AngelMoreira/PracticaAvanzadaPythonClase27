# Diccionario global para almacenar el inventario
inventario = {}

# Función para agregar productos
def agregar_producto():
    producto = input("Ingresa el nombre del producto: ")
    cantidad = int(input("Ingresa la cantidad del producto: "))
    if producto in inventario:  # Bifurcación doble
        inventario[producto] += cantidad
    else:
        inventario[producto] = cantidad
    print(f"Producto {producto} agregado con éxito!")

# Función para eliminar productos
def eliminar_producto():
    producto = input("Ingresa el nombre del producto a eliminar: ")
    if producto in inventario:  # Bifurcación simple
        del inventario[producto]
        print(f"Producto {producto} eliminado con éxito!")
    else:
        print(f"El producto {producto} no está en el inventario.")

# Función para mostrar el inventario
def mostrar_inventario():
    if len(inventario) == 0:  # Bifurcación doble
        print("El inventario está vacío.")
    else:
        print("Inventario de productos:")
        for producto, cantidad in inventario.items():  # Bucle for
            print(f"{producto}: {cantidad} unidades")

# Nueva función para actualizar la cantidad de un producto existente
def actualizar_producto():
    producto = input("Ingresa el nombre del producto a actualizar: ")
    if producto in inventario:  # Bifurcación simple
        nueva_cantidad = int(input("Ingresa la nueva cantidad: "))
        inventario[producto] = nueva_cantidad
        print(f"Producto {producto} actualizado con éxito a {nueva_cantidad} unidades!")
    else:
        print(f"El producto {producto} no está en el inventario.")

# Función principal que controla el menú
def main():
    while True:  # Bucle while
        print("\nMenú de Inventario")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Mostrar inventario")
        print("4. Actualizar cantidad de producto")
        print("5. Salir")
        opcion = input("Elige una opción: ")
        
        if opcion == '1':
            agregar_producto()
        elif opcion == '2':
            eliminar_producto()
        elif opcion == '3':
            mostrar_inventario()
        elif opcion == '4':
            actualizar_producto()
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor elige nuevamente.")

# Llamamos a la función principal
main()