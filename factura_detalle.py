class FacturaDetalle:
    """ Clase que construye el detalle de una factura """

    def __init__(self, codigo, nombre, cantidad, precio):
        self.codigo:str = codigo
        self.nombre:str = nombre
        self.cantidad:float = cantidad
        self.precio:float = precio
        self.base_imponible:float = (self.precio*self.cantidad)/1.18
        self.igv:float = (self.precio*self.cantidad)-self.base_imponible
        self.total:float = self.precio*self.cantidad
        print(self.convertir_a_string())
        pass

    def convertir_a_string(self):
        return print("|CODIGO: {} |NOMBRE: {} |CANTIDAD: {} |PRECIO: {} |BASE IMPONIBLE: {} |IGV: {} |TOTAL: {} |".format(self.codigo, self.nombre, self.precio, self.base_imponible, self.igv, self.cantidad, self.total))
