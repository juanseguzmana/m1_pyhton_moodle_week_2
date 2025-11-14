# Lista global para almacenar todos los productos como diccionarios
stock = []
def add_product():
    #Función para agregar un nuevo producto al inventario
    print("\nAGREGAR NUEVO PRODUCTO") 
    # Validación del nombre del producto
    while True:
        name = input("Nombre del producto: ").strip()
        if name == "":
            print("Error: El nombre no puede estar vacío")
            continue
        else:
            break
    # Validación del precio del producto
    while True:
        try:
            price = float(input("Precio del producto: $"))
            if price <= 0:
                print("Error: Ingrese un precio mayor a 0")
                continue
            else:
                break
        except ValueError:
            print("Error: Ingrese un número válido para el precio")  
    # Validación de la cantidad del producto
    while True:
        try:
            quantity = int(input("Cantidad del producto: "))
            if quantity <= 0:
                print("Error: Ingrese una cantidad mayor a 0")
                continue
            else:
                break
        except ValueError:
            print("Error: Ingrese un número entero válido para la cantidad")  
    # Crear diccionario con los datos del producto
    product = {
        "name": name,
        "price": price,
        "quantity": quantity
    }   
    # Agregar producto a la lista de inventario
    stock.append(product)  
    # Mostrar confirmación
    total_cost = price * quantity
    print(f"\nPRODUCTO AGREGADO EXITOSAMENTE:")
    print(f"   Producto: {name} | Precio: ${price} | Cantidad: {quantity} | Total: ${total_cost}")
def show_stock():
    #Función para mostrar todos los productos del inventario
    print("\nINVENTARIO ACTUAL")
    # Verificar si el inventario está vacío
    if len(stock) == 0:
        print("El inventario está vacío")
        print("Use la opción 1 para agregar productos")
        return
    # Mostrar todos los productos usando bucle for
    print(f"Total de productos diferentes: {len(stock)}")
    print(" ")
    for i, product in enumerate(stock, 1):
        product_total = product['price'] * product['quantity']
        print(f"{i}. {product['name']} | Precio: ${product['price']} | Cantidad: {product['quantity']} | Total: ${product_total}")
    print(" ")
def calculate_statistics():
    #Función para calcular y mostrar estadísticas del inventario
    print(" ")
    print("ESTADÍSTICAS DEL INVENTARIO")
    print(" ")   
    # Verificar si el inventario está vacío
    if len(stock) == 0:
        print("No hay productos registrados para calcular estadísticas")
        print("Use la opción 1 para agregar productos")
        return    
    # Calcular el valor total del inventario
    total_stock_value = 0
    total_units = 0    
    for product in stock:
        product_value = product['price'] * product['quantity']
        total_stock_value += product_value
        total_units += product['quantity']    
    # Mostrar resultados estadísticos
    print(f"ESTADÍSTICAS:")
    print(f"   • Productos diferentes registrados: {len(stock)}")
    print(f"   • Total de unidades en inventario: {total_units}")
    print(f"   • Valor total del inventario: ${total_stock_value:.2f}")    
    # Producto con mayor valor total
    if stock:
        highest_value_product = max(stock, key=lambda x: x['price'] * x['quantity'])
        highest_value = highest_value_product['price'] * highest_value_product['quantity']
        print(f"   • Producto con mayor valor: {highest_value_product['name']} (${highest_value:.2f})")
def main():
    #Función principal que contiene el menú interactivo
    print(" ")
    print("SISTEMA DE GESTIÓN DE INVENTARIO")
    print(" ")
    print("Bienvenido al sistema de gestión de inventario")
    print("Puede agregar productos, ver el inventario y calcular estadísticas")   
    # Bucle principal del menú
    while True:
        # Mostrar opciones del menú
        print(" ")
        print("MENÚ PRINCIPAL")
        print(" ")
        print("1. Agregar producto al inventario")
        print("2. Mostrar todos los productos del inventario")
        print("3. Calcular estadísticas del inventario")
        print("4. Salir del sistema")
        print(" ")
        # Solicitar opción al usuario
        option = input("Seleccione una opción (1-4): ").strip()   
        # Procesar la opción seleccionada usando condicionales
        if option == "1":
            add_product()
        elif option == "2":
            show_stock()
        elif option == "3":
            calculate_statistics()
        elif option == "4":
            print(" ")
            print("¡GRACIAS POR USAR EL SISTEMA DE INVENTARIO!")
            print(f"Productos registrados: {len(stock)}")
            print("¡Hasta la próxima!")
            print(" ")
            break
        else:
            # Manejo de opción inválida
            print("ERROR: Opción inválida")
            print("Por favor, seleccione una opción entre 1 y 4")
# Punto de entrada principal del programa
if __name__ == "__main__":
    main()