from collections import namedtuple
import csv
import matplotlib.pyplot as plt

RegistroPoblacion = namedtuple('RegistroPoblacion', 'pais, codigo, año, censo')

def lee_poblaciones(ruta_fichero):
    with open(ruta_fichero, encoding='utf-8') as f:
        lector = csv.reader(f)
        poblaciones = []
        for campos in lector:
            registro = RegistroPoblacion(
                campos[0],
                campos[1],
                int(campos[2]),
                int(campos[3]))
            poblaciones.append(registro)
    return poblaciones

def calcula_paises(poblaciones):
    paises = set()
    for registro in poblaciones:
        paises.add(registro.pais)
    return sorted(list(paises))

def filtra_por_pais(poblaciones, nombre_o_codigo):
    paises_filtrados = []
    for registro in poblaciones:
        if registro.pais == nombre_o_codigo or registro.codigo == nombre_o_codigo:
            paises_filtrados.append((registro.año, registro.censo))
    return paises_filtrados

def filtra_por_paises_y_anyo(poblaciones, año, paises):
    lista = []
    for registro in poblaciones:
        if registro.pais in paises and año == registro.año:
            lista.append((registro.pais, registro.censo))
    return lista

def muestra_evolucion_poblacion(poblaciones, nombre_o_codigo):
    filtrado = filtra_por_pais(poblaciones, nombre_o_codigo)
    lista_años = []
    lista_habitantes = []
    for año, censo in filtrado:
        lista_años.append(año)
        lista_habitantes.append(censo)
    plt.title('Evolución de población')
    plt.plot(lista_años, lista_habitantes)
    plt.show()

def muestra_comparativa_paises_anyo(poblaciones, año, paises):
    filtrado = filtra_por_paises_y_anyo(poblaciones, año, paises)
    lista_paises = []
    lista_habitantes = []
    for pais, censo in filtrado:
        lista_paises.append(pais)
        lista_habitantes.append(censo)
    plt.title('Comparación del censo de países')
    plt.bar(lista_paises, lista_habitantes)
    plt.show()