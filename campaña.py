from anuncio import Video, Display, Social
from error import LargoExcedidoException

class Campaña:
    def __init__(self, nombre, anuncios_data):
        self._nombre = None
        self.nombre = nombre  # Usar el setter para validar
        self.anuncios = []
        self._crear_anuncios(anuncios_data)

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if len(valor) > 250:
            raise LargoExcedidoException("El nombre de la campaña excede los 250 caracteres.")
        self._nombre = valor

    def _crear_anuncios(self, anuncios_data):
        for anuncio_data in anuncios_data:
            tipo = anuncio_data['tipo']
            sub_tipo = anuncio_data['sub_tipo']
            if tipo == 'Video':
                anuncio = Video(sub_tipo, anuncio_data['duracion'])
            elif tipo == 'Display':
                anuncio = Display(sub_tipo)
            elif tipo == 'Social':
                anuncio = Social(sub_tipo)
            else:
                continue
            self.anuncios.append(anuncio)

    def __str__(self):
        conteo_anuncios = {
            'Video': 0,
            'Display': 0,
            'Social': 0
        }
        for anuncio in self.anuncios:
            if isinstance(anuncio, Video):
                conteo_anuncios['Video'] += 1
            elif isinstance(anuncio, Display):
                conteo_anuncios['Display'] += 1
            elif isinstance(anuncio, Social):
                conteo_anuncios['Social'] += 1

        return f"Nombre de la campaña: {self.nombre}\n" \
               f"Anuncios: {conteo_anuncios['Video']} Video, {conteo_anuncios['Display']} Display, {conteo_anuncios['Social']} Social"
