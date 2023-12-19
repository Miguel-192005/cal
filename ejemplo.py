

#clase princiál 
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        pass

    def __str__(self):
        return f"Soy un animal llamado {self.nombre}"

#clase padres
class Mamifero(Animal):
    def __init__(self, nombre, tipo_pelo):
        super().__init__(nombre)
        self.tipo_pelo = tipo_pelo

    def amamantar(self):
        return "Estoy amamantando a mi cría"


class Ave(Animal):
    def __init__(self, nombre, tipo_plumaje):
        super().__init__(nombre)
        self.tipo_plumaje = tipo_plumaje

    def volar(self):
        return "Estoy volando"

#clases hijas 
class Perro(Mamifero):
    def hacer_sonido(self):
        return "Guau"


class Gato(Mamifero):
    def hacer_sonido(self):
        return "Miau"


class Aguila(Ave):
    def hacer_sonido(self):
        return "Grito de águila"


# Sobrecarga del operador suma para concatenar nombres de animales
def sumar_nombres(animal1, animal2):
    if isinstance(animal1, Animal) and isinstance(animal2, Animal):
        return f"{animal1.nombre} y {animal2.nombre}"
    else:
        raise TypeError("Ambos objetos deben ser de tipo Animal")


# Crear instancias de las clases
perro = Perro("Buddy", "Corto")
gato = Gato("Whiskers", "Largo")
aguila = Aguila("Thunder", "Plumas largas")

# Utilizar polimorfismo
print(perro.hacer_sonido())  # Salida: Guau
print(gato.hacer_sonido())   # Salida: Miau
print(aguila.hacer_sonido()) # Salida: Grito de águila

# Utilizar herencia
print(perro.amamantar())  # Salida: "Estoy amamantando a mi cría" (heredado de Mamifero)

# Utilizar sobrecarga de operadores
try:
    resultado = sumar_nombres(perro, gato)
    print(resultado)  # Salida: Buddy y Whiskers
except TypeError as e:
    print(e)
