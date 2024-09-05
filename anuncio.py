from abc import ABC, abstractmethod
from error import SubTipoInvalidoException

class Anuncio(ABC):
    def __init__(self, ancho, alto, sub_tipo):
        self._ancho = max(1, ancho)
        self._alto = max(1, alto)
        self._sub_tipo = sub_tipo

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, valor):
        if valor > 0:
            self._ancho = valor
        else:
            self._ancho = 1

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, valor):
        if valor > 0:
            self._alto = valor
        else:
            self._alto = 1

    @property
    def sub_tipo(self):
        return self._sub_tipo

    @sub_tipo.setter
    def sub_tipo(self, valor):
        if valor not in self.SUB_TIPOS:
            raise SubTipoInvalidoException("Subtipo no válido")
        self._sub_tipo = valor

    @staticmethod
    def mostrar_formatos():
        formatos = {
            'Video': Video.SUB_TIPOS,
            'Display': Display.SUB_TIPOS,
            'Social': Social.SUB_TIPOS
        }
        for formato, subtipos in formatos.items():
            print(f"FORMATO {formato}:")
            print("="*20)
            for subtipo in subtipos:
                print(f"- {subtipo}")

class Video(Anuncio):
    SUB_TIPOS = ('instream', 'outstream')

    def __init__(self, sub_tipo, duracion):
        super().__init__(1, 1, sub_tipo)
        self.duracion = max(5, duracion)

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("RECORTE DE VIDEO NO IMPLEMENTADO AÚN")

class Display(Anuncio):
    SUB_TIPOS = ('tradicional', 'native')

    def __init__(self, sub_tipo):
        super().__init__(1, 1, sub_tipo)

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADO AÚN")

class Social(Anuncio):
    SUB_TIPOS = ('Instagram', 'Facebook')

    def __init__(self, sub_tipo):
        super().__init__(1, 1, sub_tipo)

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADO AÚN")
