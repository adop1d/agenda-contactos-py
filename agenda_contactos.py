def mostrar_menu():
    print("\nAgenda de Contactos\n")
    print("1. Agregar Contacto")
    print("2. Eliminar Contacto")
    print("3. Buscar Contacto")
    print("4. Lista de Contacto")
    print("5. Salir del programa")
    print("\n")

def agregar_contacto(agenda):
    nombre = input("Ingrese el nombre completo del contacto: ")
    telefono = input("Ingrese el número de teléfono: ")
    email = input("Ingrese el correo electrónico: ")
    agenda[nombre] = {'telefono': telefono, 'email': email}
    print(f"Contacto {nombre} agregado.")

def eliminar_contacto(agenda):
    nombre = input("Ingrese el nombre completo del contacto a eliminar: ")
    if nombre in agenda:
        del agenda[nombre]
        print(f"Contacto {nombre} eliminado.")
    else:
        print(f"Contacto {nombre} no encontrado.")

def buscar_contacto(agenda):
    nombre = input("Ingrese el nombre completo del contacto a buscar: ")
    if nombre in agenda:
        print(f"Contacto encontrado: {nombre} - Teléfono: {agenda[nombre]['telefono']}, Email: {agenda[nombre]['email']}")
    else:
        print(f"Contacto {nombre} no encontrado.")

def listar_contactos(agenda):
    if agenda:
        print("\nLista de Contactos:")
        for nombre, info in agenda.items():
            print(f"{nombre} - Teléfono: {info['telefono']}, Email: {info['email']}")
            print("-" * 70)
    else:
        print("La agenda está vacía.")

def agenda_contactos():
    agenda = {}
    while True:
        mostrar_menu()
        opt = input("Seleccione una opción (1-5): ")
        print("\n")

        if opt == '1':
            agregar_contacto(agenda)
        elif opt == '2':
            eliminar_contacto(agenda)
        elif opt == '3':
            buscar_contacto(agenda)
        elif opt == '4':
            listar_contactos(agenda)
        elif opt == '5':
            print("Saliendo del programa... Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

agenda_contactos()