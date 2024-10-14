from poblacion import *

def test_lee_poblaciones(ruta_fichero):
    print("===> Test de lee_poblaciones")
    datos = lee_poblaciones(ruta_fichero)
    print(f"Leídos {len(datos)} registros.")
    print("\nMostrando los 3 primeros:")
    print(datos[:3])
    print("\nMostrando los 3 últimos")
    print(datos[-3:])
    return datos

def test_calcula_paises(poblaciones):
    print("===> Test de  calcula_paises")
    datos = calcula_paises(poblaciones)
    print(f"Obtenidos {len(datos)} países.")
    print("\nMostrando los 3 primeros:")
    print(datos[:3])
    print("\nMostrando los 3 últimos")
    print(datos[-3:])

def test_filtra_por_pais(poblaciones, nombre_o_codigo):
    print("===> Test de  filtra_por_pais")
    datos = filtra_por_pais(poblaciones, nombre_o_codigo)
    print(f"Obtenidos {len(datos)} datos del país.")
    print("\nMostrando los 3 primeros:")
    print(datos[:3])
    print("\nMostrando los 3 últimos")
    print(datos[-3:])

def test_filtra_por_paises_y_anyo(poblaciones, año, paises):
    print("===> Test de  filtra_por_paises_y_anyo")
    datos = filtra_por_paises_y_anyo(poblaciones, año, paises)
    print(f"Obtenidos {len(datos)} datos de poblaciones.")
    print("\nMostrando los 3 primeros:")
    print(datos[:3])
    print("\nMostrando los 3 últimos")
    print(datos[-3:])


if __name__ == '__main__':
    poblaciones = lee_poblaciones('data/population.csv')
    nombre_o_codigo = 'ESP'
    paises = {'Spain', 'Zimbabwe', 'Turkey'}

    #   test_lee_poblaciones('data/population.csv')
    #   test_calcula_paises(poblaciones)
    #   test_filtra_por_pais(poblaciones, nombre_o_codigo)
    #   test_filtra_por_paises_y_anyo(poblaciones, 2016, paises)
    #   muestra_evolucion_poblacion(poblaciones, nombre_o_codigo)
    muestra_comparativa_paises_anyo(poblaciones, 2016, paises)