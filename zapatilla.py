class Zapatilla:
    """ Clase que construye zapatilla """

    def __init__(self, codigo, precio, marca, talla, color, actividad):
        self.codigo: str = codigo
        self.precio: str = precio
        self.marca: str = marca
        self.talla: str = talla
        self.color: str = color
        self.actividad: str = actividad
        print(self.convertir_a_string())
        pass

    def convertir_a_string(self):
        return print("| {} | {} | {} | {} | {} | {} |".format(self.codigo, self.precio, self.marca, self.talla, self.color, self.actividad))
