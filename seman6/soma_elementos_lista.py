import pytest

def soma_lista(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return lista[0] + soma_lista(lista[1:])
        
@pytest.mark.parametrize('entrada, esperado', [
    ([0], 0),
    ([0, 1], 1),
    ([0, 0, 0, 0], 0),
    ([41, 48, 463, 995, 719, 356, 542, 808, 754, 794, 920], 6440)
    ])

def testa_soma_elementos (entrada, esperado):
    assert soma_lista(entrada) == esperado
