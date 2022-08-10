## Este script conta e compara o tempo de execução dos métodos buscadores
## Busca Sequencial e Busca Binaria, para comparar a eficicência de ambos.

import time
import random
import buscador


class conta_tempos_buscador:
    def lista_aleatoria(self, n):
        lista = [random.randrange(100000) for x in range(n)]
        return lista

    def compara(self, n, elemento):
        lista1 = self.lista_aleatoria(n)
        
        b = buscador.Buscador()
        
        # Testando método busca sequencial.

        antes = time.time()
        b.busca_binaria(lista1, elemento)
        depois = time.time()
        print('Método Busca Binaria demorou', depois - antes)
        
        antes = time.time()
        b.busca_sequencial(lista1, elemento)
        depois = time.time()
        print('Método Busca Sequencial demorou', depois - antes)


        

        

