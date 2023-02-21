class Estado:
    """Clase que representa un estado en el autómata"""
    def __init__(self, num):
        self.numero = num

    def __str__(self):
        return str(self.numero)