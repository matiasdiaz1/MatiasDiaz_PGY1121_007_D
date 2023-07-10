



ubicaciones = []
vendidas = [False] 
run = [None] 

 
def menu():
    while True:
        print("----- Menú -----")
        print("1. Comprar entradas")
        print("2. Mostrar ubicaciones disponibles")
        print("3. Ver listado de asistentes")
        print("4. Mostrar ganancias totales")
        print("5. Salir")
        opcion = int(input("Seleccione una opción: "))
        match opcion:
            case 1:
                comprar_entradas()
            case 2:
                  mostrar_ubicaciones()
            case 3:
                  ver_listado()
            case 4:
                  pass
            case 5:
                  break
            case other:
                  print("opcion no valida")




def comprar_entradas():
    cantidad = input("Ingrese la cantidad de entradas a comprar (1-3): ")
    while True:
        if cantidad.isdigit() and 1 <= int(cantidad) <= 3:
            break
        cantidad = input("Cantidad inválida. Ingrese la cantidad de entradas a comprar (1-3): ")
    cantidad = int(cantidad)

  
    print("Ubicaciones disponibles:")
    for i in range(len(ubicaciones)):
        if not vendidas[i]:
            print(f"{i+1}. {ubicaciones[i]}")
        else:
            print(f"{i+1}. X")

   
    for i in range(cantidad):
        ubicacion = input(f"Ingrese la ubicación para la entrada {i+1}: ")
        while True:
            if ubicacion.isdigit() and 1 <= int(ubicacion) <= 100 and not vendidas[int(ubicacion)-1]:
                break
            ubicacion = input(f"Ubicación no disponible. Ingrese la ubicación para la entrada {i+1}: ")
        vendidas[int(ubicacion)-1] = True
        run[int(ubicacion)-1] = input(f"Ingrese el RUT para la entrada {i+1}: ")

   
    print("La operacion se realizo bien")


def mostrar_ubicaciones():
    print("Ubicaciones disponibles:")
    for i in range(len(ubicaciones)):
        if not vendidas[i]:
            print(f"{i+1}. {ubicaciones[i]}")
        else:
            print(f"{i+1}. X")


def ver_listado():
    asistentes = [(run[i], i+1) for i in range(len(run)) if run[i] is not None]
    asistentes.sort()
    print("Listado de asistentes:")









    