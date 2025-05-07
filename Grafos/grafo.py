import os


class Noh:
    def __init__(self, rotulo: str):
        self.rotulo = rotulo
        self.visitado = False
        self.adjacentes: list[Adjacente] = []

    def adicionar_adjacente(self, adjacente):
        self.adjacentes.append(adjacente)

    def mostrar_adjacentes(self) -> str:
        impressao = f"{'Noh':>8}|Peso\n"
        for a in self.adjacentes:
            impressao += f"{a.noh.rotulo:>8}|{a.peso}\n"

        return impressao

    def __str__(self) -> str:
        return f"{self.rotulo:.^18}\n{self.mostrar_adjacentes()}"


class Adjacente:
    def __init__(self, noh: Noh, peso: int):
        self.noh = noh
        self.peso = peso


class Grafo:

    def __init__(self, noh: Noh = None):
        self._comprimento = 0
        self.noh: Noh = noh
        self.buscar_noh = False

    @property
    def comprimento(self) -> int:
        self.desvisitar_grafo(self.noh)
        self._comprimento = 0
        self._comprimento = self.checar_comprimento(self.noh)
        return self._comprimento

    @comprimento.setter
    def comprimento(self, novo_valor: int):
        self._comprimento = novo_valor

    def inserir_noh(self) -> bool:
        novo_rotulo = input("Rótulo do novo noh: ")
        self.desvisitar_grafo(self.noh)
        self.buscar_noh = True
        if self.encontrar_noh(noh=self.noh, rotulo=novo_rotulo):
            return False
        novo_noh = Noh(novo_rotulo)
        if not self.noh:
            self.noh = novo_noh
            return True

        return self.aresta_novo_noh(novo_noh)

    def aresta_novo_noh(self, novo_noh: Noh) -> bool:
        self.imprimir()
        rotulo = input("Selecione o noh: ")
        self.desvisitar_grafo(self.noh)
        self.buscar_noh = True
        noh_selecionado = self.encontrar_noh(noh=self.noh, rotulo=rotulo)
        if not noh_selecionado:
            return False  # Noh ausente no grafo
        custo_peso = input("Informe custo/peso: ")
        adj = Adjacente(novo_noh, custo_peso)
        noh_selecionado.adicionar_adjacente(adj)
        adj = Adjacente(noh_selecionado, custo_peso)
        novo_noh.adicionar_adjacente(adj)
        return True

    def setar_arestas(self) -> bool:
        self.imprimir()
        rotulo1 = input("Primeiro noh: ")
        rotulo2 = input("Segundo noh: ")
        self.desvisitar_grafo(self.noh)
        self.buscar_noh = True
        noh1 = self.encontrar_noh(noh=self.noh, rotulo=rotulo1)
        self.desvisitar_grafo(self.noh)
        self.buscar_noh = True
        noh2 = self.encontrar_noh(noh=self.noh, rotulo=rotulo2)
        if not (noh1 and noh2):
            return False  # Noh ausente no grafo
        custo_peso = input("Informe custo/peso: ")
        adj = Adjacente(noh1, custo_peso)
        noh2.adicionar_adjacente(adj)
        adj = Adjacente(noh2, custo_peso)
        noh1.adicionar_adjacente(adj)
        return True

    def checar_comprimento(self, noh_inicial: Noh = None) -> int:
        if noh_inicial:
            # noh_inicial = self.noh
            if not noh_inicial.visitado:
                self._comprimento += 1
                noh_inicial.visitado = True
                for adjacente in noh_inicial.adjacentes:
                    self.checar_comprimento(adjacente.noh)

        return self._comprimento

    def percorrer_e_imprimir(self, noh_inicial: Noh = None) -> None:
        if noh_inicial:
            if not noh_inicial.visitado:
                print(noh_inicial)
                noh_inicial.visitado = True
                for adjacente in noh_inicial.adjacentes:
                    self.percorrer_e_imprimir(adjacente.noh)

    def imprimir(self):
        self.desvisitar_grafo(self.noh)
        self.percorrer_e_imprimir(self.noh)
        # self.desvisitar_grafo(self.noh)

    def imprimir_de_noh(self) -> bool:
        rotulo = input("Imprimir a partir de qual Noh? ")
        self.desvisitar_grafo(self.noh)
        self.buscar_noh = True
        noh = self.encontrar_noh(noh=self.noh, rotulo=rotulo)
        if not noh:
            return False
        self.desvisitar_grafo(self.noh)
        self.buscar_noh = True
        self.percorrer_e_imprimir(noh)
        return True

    def desvisitar_grafo(self, noh: Noh):
        if noh:
            if noh.visitado:
                noh.visitado = False
                for adjacente in noh.adjacentes:
                    self.desvisitar_grafo(adjacente.noh)

    def encontrar_noh(self, rotulo: str, noh: Noh = None) -> Noh:
        if not self.noh:
            return None

        if not noh:
            noh = self.noh

        if self.buscar_noh:
            if not noh.visitado:
                if noh.rotulo == rotulo:
                    self.buscar_noh = False
                    return noh
                noh.visitado = True
                for adjacente in noh.adjacentes:
                    resultado = self.encontrar_noh(rotulo, adjacente.noh)
                    if resultado:
                        return resultado
        return None

    def remover_noh(self):
        self.imprimir()
        rotulo = input("Noh a ser removido: ")
        self.desvisitar_grafo(self.noh)
        self.buscar_noh = True
        noh = self.encontrar_noh(noh=self.noh, rotulo=rotulo)
        if not noh:
            return False  # Noh ausente no grafo

        if noh == self.noh:
            self.noh = noh.adjacentes[0].noh

        for adj1 in noh.adjacentes:
            for adj2 in adj1.noh.adjacentes:
                if adj2.noh == noh:
                    adj1.noh.adjacentes.remove(adj2)

        return True


if __name__ == "__main__":
    noh_a = Noh("A")
    noh_b = Noh("B")
    noh_c = Noh("C")
    noh_d: Noh = Noh("D")
    noh_e = Noh("E")
    noh_f = Noh("F")
    noh_a.adicionar_adjacente(Adjacente(noh_b, 2))
    noh_b.adicionar_adjacente(Adjacente(noh_a, 2))
    noh_b.adicionar_adjacente(Adjacente(noh_c, 3))
    noh_b.adicionar_adjacente(Adjacente(noh_d, 1))
    noh_c.adicionar_adjacente(Adjacente(noh_b, 3))
    noh_c.adicionar_adjacente(Adjacente(noh_d, 1))
    noh_c.adicionar_adjacente(Adjacente(noh_e, 2))
    noh_d.adicionar_adjacente(Adjacente(noh_b, 1))
    noh_d.adicionar_adjacente(Adjacente(noh_c, 1))
    noh_d.adicionar_adjacente(Adjacente(noh_f, 3))
    noh_f.adicionar_adjacente(Adjacente(noh_d, 3))
    noh_f.adicionar_adjacente(Adjacente(noh_e, 4))
    noh_e.adicionar_adjacente(Adjacente(noh_c, 2))
    noh_e.adicionar_adjacente(Adjacente(noh_f, 4))
    grafo = Grafo(noh=noh_a)

    menu = """
        [0] Sair                        [4] Esvaziar o grafo;
        [1] Inserir nó;                 [5] Imprimir a partir de um determinado nó;
        [2] Remover nó;                 [6] Tamanho (quantidade de nós);
        [3] Encontrar determinado nó;   [7] Setar arestas.
    """

    while True:
        os.system("cls")

        print(menu)

        opcao = input("\n\tOpção: ")

        match opcao:
            case "0":  # Sair
                break
            case "1":  # Inserir nó
                os.system("cls")
                print(f"Novo noh inserido com sucesso? {grafo.inserir_noh()}")
                input()
            case "2":  # Remover nó
                os.system("cls")
                print(f"Noh removido com sucesso? {grafo.remover_noh()}")
                input()
            case "3":  # Encontrar determinado nó
                os.system("cls")
                grafo.desvisitar_grafo(grafo.noh)
                rotulo = input("Rótulo: ")
                grafo.buscar_noh = True
                print(f"{grafo.encontrar_noh(noh=grafo.noh, rotulo=rotulo)}")
                input()
            case "4":  # Esvaziar o grafo
                os.system("cls")
                grafo.noh = None
                input()
            case "5":  # Imprimir a partir de um determinado nó
                os.system("cls")
                resultado = (
                    "Sucesso na impressão!"
                    if grafo.imprimir_de_noh()
                    else "Falha na impressão"
                )
                print(f"\n\t{resultado}\n")
                input()
            case "6":  # Tamanho (quantidade de nós)
                os.system("cls")
                print(f"{grafo.comprimento = }")
                input()
            case "7":  # Setar arestas
                os.system("cls")
                print(f"Nova aresta setada com sucesso? {grafo.setar_arestas()}")
                input()
