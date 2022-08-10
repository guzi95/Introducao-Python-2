import ordenador
import pytest

class TestOrdenador:
    @pytest.fixture
    def x(self):
        return ordenador.Ordenador()
    
    @pytest.mark.parametrize("entrada, resultado", [
        ([2, 3, 1], ([1, 2, 3])),
        ([7, 4, 451, 100, 200], ([4, 7, 100, 200, 451])),
        ([53, 68, 12, 40], ([12, 40, 53, 68]))
        ])

    def testa_ordenador(self, x, entrada, resultado):
        assert x.bolha(entrada) == resultado
