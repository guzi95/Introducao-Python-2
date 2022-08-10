## Recebe uma lista de numeros inteiros e devolve os valores ímpares.

def encontra_impares(lista):
    if len(lista) == 1:
        if (lista[0] % 2) != 0:
            impar = [lista[0]]
            return impar
        else:
            return []    
    else:
        lista_impares = []
        lista_impares.extend(encontra_impares([lista[0]]) + encontra_impares(lista[1:]))
        return lista_impares

import pytest
@pytest.mark.parametrize('entrada, esperado', [
    ([1, 2, 3, 4, 5, 6], [1, 3, 5]),
    ([0, 1, 2, 3, 4, 5], [1, 3, 5]),
    ([0], []),
    ([0, 2, 4], [])
    ])

def testa_encontra_impares(entrada, esperado):
    assert encontra_impares(entrada) == esperado
    
    
