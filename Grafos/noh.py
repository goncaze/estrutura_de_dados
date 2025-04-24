class Noh:
    def __init__(self, rotulo: str):
        self.rotulo = rotulo
        self.visitado = False
        self.adjacentes: list[Adjacente] = []

    def adicionar_adjacente(self, adjacente: Adjacente):
        self.adjacentes.append(adjacente)

    def mostrar_adjacentes(self):
        for a in self.adjacentes:
            print(a.noh.rotulo)
            print(a.peso)
