"""
ESTRUTURA DE DADOS
ATIVIDADE DE LISTA ENCADEADA SIMPLES COM POO

==>>> // Não usar Inteligência Artificial \\ <<<==

Caro estudante de TDS, você deverá criar um menu interativo para realização das
seguintes operações da lista encadeada simples:

1. Criar uma classe Nodo.
2. Criar uma classe Lista.

3. Criar uma função que verifica se a lista está vazia.
4. Criar uma função que informa o tamanho da lista
5. Criar uma função que adiciona um elemento no início da lista.
6. Criar uma função que adiciona um elemento no final da lista.
7. Criar uma função que adiciona um elemento em uma posição específica da lista.
8. Criar uma função que remove um elemento em uma posição específica da lista.
9. Criar uma função que remove o primeiro elemento da lista.
10.Criar uma função que remove o último elemento da lista.
11.Criar uma função que conta o número de ocorrências de um elemento na lista

OBSERVAÇÃO: a número 11 fica por conta de vocês. Não utilizar Inteligência Artificial.
"""

import os


# 1.  Criar uma classe Nodo.
class Noh:
    def __init__(self, valor=None, prox=None):
        self.valor = valor
        self.prox: Noh = prox

    def __str__(self) -> str:
        return f"[{self.valor}] => {self.prox}"


# 2.  Criar uma classe Lista.
class Lista:
    def __init__(self, primeiro_noh: Noh = None):
        self.primeiro_noh: Noh = primeiro_noh

    # 3.  Criar uma função que verifica se a lista está vazia.
    def esta_vazia(self) -> bool: ...

    # 4.  Criar uma função que informa o tamanho da lista
    def comprimento(self) -> int: ...

    # 5.  Criar uma função que adiciona um elemento no início da lista.
    def insert(self, novo_noh: Noh): ...

    # 6.  Criar uma função que adiciona um elemento no final da lista.
    def append(self, novo_noh: Noh): ...

    # 7. Criar uma função que adiciona um elemento em uma posição específica da lista.
    def colocar_em_p(self, posicao: int, novo_noh: Noh) -> bool: ...

    # 8. Criar uma função que remove um elemento em uma posição específica da lista.
    def remover_em_p(self, posicao: int) -> bool: ...

    # 9.  Criar uma função que remove o primeiro elemento da lista.
    def remover_primeiro(self) -> bool: ...

    # 10. Criar uma função que remove o último elemento da lista.
    def remover_ultimo(self) -> bool: ...

    # 11. Criar uma função que conta o número de ocorrências de um elemento na lista
    # ==> ITEM 11 É UMA ATIVIDADE PARA OS ALUNOS DE TDS <==
    def contar_ocorrencias(self, elemento) -> bool: ...

    def __str__(self) -> str:
        return f"{self.primeiro_noh}"


# ======================================================== #
# ================= CONTROLE DE MENU ===================== #


def controle_menu(): ...


# ======================================================== #
# =================== INVOCAR FUNÇÃO ===================== #
if __name__ == "__main__":

    controle_menu()
