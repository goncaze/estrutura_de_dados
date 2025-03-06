"""
ESTRUTURA DE DADOS
ATIVIDADE DE LISTA ENCADEADA SIMPLES COM POO

==>>> // Não usar Inteligência Artificial \\ <<<==

Caro estudante de TDS, você deverá criar um menu interativo para realização das
seguintes operações da lista encadeada simples:

1. Criar uma classe Noh.
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
    def esta_vazia(self) -> bool:
        return self.primeiro_noh is None

    # 4.  Criar uma função que informa o tamanho da lista
    def comprimento(self) -> int:
        i = 0
        nohaux: Noh = self.primeiro_noh
        while True:
            if nohaux:
                i += 1
                nohaux = nohaux.prox
            else:
                break
        return i

    # 5.  Criar uma função que adiciona um elemento no início da lista.
    def insert(self, novo_noh: Noh):
        novo_noh.prox = self.primeiro_noh
        self.primeiro_noh = novo_noh

    # 6.  Criar uma função que adiciona um elemento no final da lista.
    def append(self, novo_noh: Noh):
        if not self.esta_vazia():  # Se lista não estiver vazia
            nohaux: Noh = self.primeiro_noh
            while True:
                if nohaux.prox:
                    nohaux = nohaux.prox
                else:
                    nohaux.prox = novo_noh
                    break
        else:
            self.primeiro_noh = novo_noh

    # 7. Criar uma função que adiciona um elemento em uma posição específica da lista.
    def colocar_em_p(self, posicao: int, novo_noh: Noh) -> bool:
        if not self.esta_vazia():
            if posicao != 0:
                nohaux: Noh = self.primeiro_noh
                i = 0
                posicao -= 1
                while nohaux:
                    if posicao != i:
                        i += 1
                        nohaux = nohaux.prox
                    else:
                        novo_noh.prox = nohaux.prox
                        nohaux.prox = novo_noh
                        return True

            elif posicao == 0:
                novo_noh.prox = self.primeiro_noh
                self.primeiro_noh = novo_noh
                return True

        return False

    # 8. Criar uma função que remove um elemento em uma posição específica da lista.
    def remover_em_p(self, posicao: int) -> bool:
        if not self.esta_vazia():
            if posicao != 0:
                nohaux: Noh = self.primeiro_noh
                i = 0
                posicao -= 1
                while nohaux:
                    if posicao != i:
                        i += 1
                        nohaux = nohaux.prox
                    else:
                        nohaux.prox = nohaux.prox.prox
                        return True
            elif posicao == 0:
                if not self.primeiro_noh.prox:
                    self.primeiro_noh = None
                else:
                    self.primeiro_noh = self.primeiro_noh.prox
                return True

        return False

    # 9.  Criar uma função que remove o primeiro elemento da lista.
    def remover_primeiro(self) -> bool:
        if not self.esta_vazia():
            self.primeiro_noh = self.primeiro_noh.prox
            return True
        return False

    # 10. Criar uma função que remove o último elemento da lista.
    def remover_ultimo(self) -> bool:
        if not self.esta_vazia():
            nohaux = self.primeiro_noh
            while nohaux.prox.prox:
                nohaux = nohaux.prox
            nohaux.prox = None
            return True

        return False

    # 11. Criar uma função que conta o número de ocorrências de um elemento na lista
    # ==> ITEM 11 É UMA ATIVIDADE PARA OS ALUNOS DE TDS <==
    def contar_ocorrencia(elemento): ...

    def __str__(self) -> str:
        return f"{self.primeiro_noh}"


# ======================================================== #
# ================= CONTROLE DE MENU ===================== #


def controle_menu(): ...


# ======================================================== #
# =================== INVOCAR FUNÇÃO ===================== #
if __name__ == "__main__":

    controle_menu()
