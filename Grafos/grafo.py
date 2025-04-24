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
    def __init__(self):

        self.noh_a = Noh("A")
        self.noh_b = Noh("B")
        self.noh_c = Noh("C")
        self.noh_d: Noh = Noh("D")
        self.noh_e = Noh("E")
        self.noh_f = Noh("F")

        self.noh_a.adicionar_adjacente(Adjacente(self.noh_b, 2))
        self.noh_b.adicionar_adjacente(Adjacente(self.noh_a, 2))
        self.noh_b.adicionar_adjacente(Adjacente(self.noh_c, 3))
        self.noh_b.adicionar_adjacente(Adjacente(self.noh_d, 1))
        self.noh_c.adicionar_adjacente(Adjacente(self.noh_b, 3))
        self.noh_c.adicionar_adjacente(Adjacente(self.noh_d, 1))
        self.noh_c.adicionar_adjacente(Adjacente(self.noh_e, 2))
        self.noh_d.adicionar_adjacente(Adjacente(self.noh_b, 1))
        self.noh_d.adicionar_adjacente(Adjacente(self.noh_c, 1))
        self.noh_d.adicionar_adjacente(Adjacente(self.noh_f, 3))
        self.noh_f.adicionar_adjacente(Adjacente(self.noh_d, 3))
        self.noh_f.adicionar_adjacente(Adjacente(self.noh_e, 4))
        self.noh_e.adicionar_adjacente(Adjacente(self.noh_c, 2))
        self.noh_e.adicionar_adjacente(Adjacente(self.noh_f, 4))

    def percorrer(self):
        print(self.noh_b)


if __name__ == "__main__":
    grafo = Grafo()
    os.system("cls")
    print()
    grafo.percorrer()
    print()
