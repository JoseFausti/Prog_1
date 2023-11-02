# 4)_Realizar una clase que administre una agenda. Se debe almacenar para cada contacto el nombre,
# el teléfono y el email. 
# Además deberá mostrar un menú con las siguientes opciones:
# Añadir contacto
# Lista de contactos
# Buscar contacto
# Editar contacto
# Cerrar agenda

# Definición de la clase Agenda que administra contactos.
class Agenda:
    def __init__(self):
        # Constructor de la clase, inicializa la lista de contactos.
        self.__contacts = []

    # Lista de contactos
    @property # Getter
    def contacts(self):
        # Método para mostrar la lista de contactos.
        # Itera sobre la lista de contactos y muestra la información de cada uno.
        for i, contact in enumerate(self.__contacts, start=1):
            print(f"Contacto {i}:")
            print(f"Nombre: {contact['nombre']}")  # Corregir 'name' a 'nombre'
            print(f"Telefono: {contact['telefono']}")  # Corregir 'phone' a 'telefono'
            print(f"Email: {contact['email']}")  # Corregir 'email' a 'email'
            print()

    # Añadir contactos
    @contacts.setter # Setter
    def contacts(self, name, phone, email):
        # Método para agregar un contacto a la agenda.
        # Crea un diccionario con los datos del contacto y lo agrega a la lista.
        contact = {"nombre": name, "telefono": phone, "email": email}
        self.__contacts.append(contact)

    # Buscar contacto
    def find_contact(self, name):
    # Método para buscar un contacto por nombre.
    # Itera sobre la lista de contactos y compara el nombre con el proporcionado.
        for contact in self.__contacts:
            if contact['nombre'] == name:  # Corregir 'name' a 'nombre'
            # Si se encuentra el contacto, muestra su información.
                print(f"Nombre: {contact['nombre']}")  # Corregir 'name' a 'nombre'
                print(f"Telefono: {contact['telefono']}")  # Corregir 'phone' a 'telefono'
                print(f"Email: {contact['email']}")  # Corregir 'email' a 'email'
                return
    # Si no se encuentra el contacto, muestra un mensaje de que no se encontró.
    print("Contacto no encontrado.")

    # Editar contacto
    def edit_contact(self, name, new_phone, new_email):
        # Método para editar un contacto.
        # Itera sobre la lista de contactos y compara el nombre con el proporcionado.
        for contact in self.__contacts:
            if contact['nombre'] == name:
                # Si se encuentra el contacto, se actualiza el número y el email
                contact['telefono'] = new_phone
                contact['email'] = new_email
                print("Contacto actualizado.")
                return
        # Si no se encuentra el contacto, se muestra un mensaje de que el contacto no fue encontrado
        print("Contacto no encontrado.")
