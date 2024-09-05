from campaña import Campaña
from anuncio import Video, Display, Social
from error import SubTipoInvalidoException, LargoExcedidoException
import logging

# Configurar el registro de errores
logging.basicConfig(filename='error.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    # Datos iniciales para la campaña
    anuncios_data = [
        {'tipo': 'Video', 'sub_tipo': 'instream', 'duracion': 10}
    ]
    
    try:
        # Crear una campaña inicial
        campaña = Campaña(nombre='Campaña Inicial', anuncios_data=anuncios_data)
        print("Campaña creada con éxito.")
        print(campaña)
        
        # Solicitar nuevo nombre de la campaña y subtipo para el anuncio
        nuevo_nombre = input("Ingrese un nuevo nombre para la campaña: ")
        nuevo_subtipo = input("Ingrese un nuevo subtipo para el anuncio de Video: ")
        
        # Modificar el nombre de la campaña
        try:
            campaña.nombre = nuevo_nombre
        except LargoExcedidoException as e:
            logging.error(f"Error al modificar el nombre de la campaña: {e}")
            print(f"Error: {e}")

        # Modificar el subtipo del anuncio
        try:
            campaña.anuncios[0].sub_tipo = nuevo_subtipo
        except SubTipoInvalidoException as e:
            logging.error(f"Error al modificar el subtipo del anuncio: {e}")
            print(f"Error: {e}")

        # Mostrar la información de la campaña después de los cambios
        print(campaña)

    except Exception as e:
        logging.error(f"Error general: {e}")
        print(f"Error general: {e}")

if __name__ == "__main__":
    main()
