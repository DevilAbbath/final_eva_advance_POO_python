class LargoExcedidoException(Exception):
    """Excepción lanzada cuando el nombre de la campaña excede el límite de caracteres."""
    def __init__(self, mensaje="El nombre de la campaña excede los 250 caracteres permitidos."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class SubTipoInvalidoException(Exception):
    """Excepción lanzada cuando el subtipo de anuncio no es válido."""
    def __init__(self, mensaje="El subtipo ingresado no es válido para este tipo de anuncio."):
        self.mensaje = mensaje
