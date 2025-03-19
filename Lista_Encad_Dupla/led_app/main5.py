import flet as ft
import string


class App:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.theme_mode = ft.ThemeMode.DARK
        self.page.auto_scroll = True
        self.page.horizontal_alignment = ft.CrossAxisAlignment.STRETCH
        self.page.window.width = 400
        self.page.window.height = 680
        self.page.window.always_on_top = True
        self.page.window.left = 1100
        self.page.window.top = 80
        self.page.padding = 10

        self.capa = ft.Image(src=r"capa2.png")
        self.txt_titulo = ft.Text(
            value="LISTA ENCADEADA SIMPLES",
            size=20,
            color=ft.colors.WHITE,
            bgcolor=ft.colors.ORANGE_800,
            weight=ft.FontWeight.NORMAL,
        )

        self.ltw_lista = ft.ListView(
            expand=1,
            auto_scroll=True,
            controls=[
                ft.Row(
                    controls=[
                        ft.Text(value=xyz, size=20),
                        ft.Text(value=abc, size=20),
                    ]
                )
                for xyz, abc in zip(range(0, 10), string.ascii_uppercase[:10])
            ],
        )

        self.ctn_lista = ft.Container(
            content=self.ltw_lista,
            expand=True,
            padding=ft.padding.only(bottom=10, top=10),
            margin=ft.margin.all(10),
        )

        self.txt_comprimento = ft.Text(
            value=f"Comprimento da lista: {len(self.ltw_lista.controls)}", size=19
        )
        self.txt_index = ft.Text(
            value="Posição específica", weight=ft.FontWeight.W_500, size=19.5
        )
        self.ttf_index = ft.TextField(label="Index", expand=True)
        self.ttf_novo_valor = ft.TextField(label="Novo valor")

        # Botão para inserir valor no final da lista
        self.btn_inserir_final = ft.CupertinoButton(
            text="Inserir final",
            on_click=self.clk_inserir_final,
            expand=True,
            border_radius=5,
            color=ft.colors.WHITE,
            bgcolor="#d5085c",
            padding=0,
        )
        # Botão para inserir valor no início da lista
        self.btn_inserir_inicio = ft.CupertinoButton(
            text="Inserir inicio",
            on_click=self.clk_inserir_inicio,
            expand=True,
            border_radius=5,
            color=ft.colors.WHITE,
            bgcolor="#d5085c",
            padding=0,
        )
        # Botão para remover valor no inicio da lista
        self.btn_remover_inicio = ft.CupertinoButton(
            text="Remover inicio",
            on_click=self.clk_remover_inicio,
            expand=True,
            border_radius=5,
            color=ft.colors.WHITE,
            bgcolor="#d5085c",
            padding=0,
        )
        # Botão para remover valor no final da lista
        self.btn_remover_final = ft.CupertinoButton(
            text="Remover final",
            on_click=self.clk_remover_final,
            expand=True,
            border_radius=5,
            color=ft.colors.WHITE,
            bgcolor="#d5085c",
            padding=0,
        )

        # Botão para inserir em posição especificada
        self.btn_inserir_especifica = ft.CupertinoButton(
            text="Inserir Específica",
            on_click=self.clk_inserir_especifica,
            expand=True,
            border_radius=5,
            color=ft.colors.WHITE,
            bgcolor="#d5085c",
            padding=0,
        )
        # Botão para remover em posição especificada
        self.btn_remover_especifica = ft.CupertinoButton(
            text="Remover Específica",
            on_click=self.clk_remover_especifica,
            expand=True,
            border_radius=5,
            color=ft.colors.WHITE,
            bgcolor="#d5085c",
            padding=0,
        )

        # Criar linha para alinhar botões
        self.ctn_controles = ft.Container(
            # expand=True,
            content=ft.Column(
                expand=True,
                controls=[
                    ft.Row(
                        expand=True,
                        controls=[
                            self.btn_inserir_inicio,
                            self.btn_inserir_final,
                        ],
                    ),
                    ft.Row(
                        controls=[
                            self.btn_remover_inicio,
                            self.btn_remover_final,
                        ]
                    ),
                    ft.Row(
                        controls=[
                            self.txt_index,
                            self.ttf_index,
                        ]
                    ),
                    ft.Row(
                        controls=[
                            self.btn_inserir_especifica,
                            self.btn_remover_especifica,
                        ],
                    ),
                ],
            ),
        )

        # Adicionando componentes na page
        self.page.add(
            ft.SafeArea(
                expand=True,
                content=ft.Column(
                    expand=True,
                    controls=[
                        self.capa,
                        # self.txt_titulo,
                        self.txt_comprimento,
                        self.ctn_lista,
                        self.ttf_novo_valor,
                        self.ctn_controles,
                    ],
                ),
            )
        )

        self.ttf_novo_valor.focus()  # Atribuir foco ao componente ttf_texto
        self.page.update()  # Atualizar/Recarregar a page

    # Função para recontar os índices da lista
    def recontar_indices(self):
        i = 0  # Contador inciando em zero
        for elemento in self.ltw_lista.controls:  # Para cada elemento da lista
            elemento.controls[0].value = i  # Atribua o atual valor da variável i
            i += 1  # Incremente com mais 1 o valor da variável i
        self.txt_comprimento.value = (
            f"Comprimento: {i}"  # Atualiza comprimento da lista
        )
        self.txt_comprimento.update()  # Atualiza estado do componente

    # Função para limpar e atualizar campos
    def limpar_atualizar_campos(self):
        self.recontar_indices()
        self.ltw_lista.update()  # Atualiza estado do componente
        self.ttf_index.value = ""
        self.ttf_index.update()
        self.ttf_novo_valor.value = ""  # Limpar campo de obtenção de dado do usuário
        self.ttf_novo_valor.focus()  # Atribuir foco ao componente ttf_texto
        self.ttf_novo_valor.update()  # Atualiza estado do componente
        self.txt_comprimento.value = f"Comprimento: {len(self.ltw_lista.controls)}"
        self.txt_comprimento.update()

    # Função decoradora para insercoes
    def preparativos_insercao(func):
        def wrapper(self, e, *args, **kwargs):
            func(self, e, *args, **kwargs)
            self.limpar_atualizar_campos()

        return wrapper

    # Função para inserir valor no final da lista
    @preparativos_insercao
    def clk_inserir_final(self, e):
        dado_usuario = self.ttf_novo_valor.value  # Obter dado do usuário
        self.ltw_lista.controls.append(  # Inserir dado_usuario no final da lista
            ft.Row(  # Cada elemento da lista é uma Row (linha)
                controls=[  # Cada linha contém dois componentes lado a lado
                    ft.Text(size=20),  # Para o índice da posição atual da lista
                    ft.Text(value=dado_usuario, size=20),  # O dado do usuário
                ]
            )
        )

    # Função para inserir dado_usuario no início da lista
    @preparativos_insercao
    def clk_inserir_inicio(self, e):
        dado_usuario = self.ttf_novo_valor.value  # Obter dado do usuário
        # Criar uma Row (linha) com índice e novo dado_usuario
        nova_linha = ft.Row(
            controls=[ft.Text(value="", size=20), ft.Text(value=dado_usuario, size=20)]
        )
        lista_aux = [nova_linha]  # Criar uma lista com a nova linha
        self.ltw_lista.controls = lista_aux + self.ltw_lista.controls

    # Função decorada para remocoes
    def preparativos_remocao(func):
        def wrapper(self, e, *args, **kwargs):
            func(self, e, *args, **kwargs)
            self.limpar_atualizar_campos()

        return wrapper

    # Função para remover valor no final da lista
    @preparativos_remocao
    def clk_remover_inicio(self, e):
        self.ltw_lista.controls.pop(0)  # remover texto no inicio da lista

    # Função para remover valor no final da lista
    @preparativos_remocao
    def clk_remover_final(self, e):
        self.ltw_lista.controls.pop()  # remover texto no final da lista

    # Função para inserir valor em posicao específica
    @preparativos_insercao
    def clk_inserir_especifica(self, e):
        dado_usuario = self.ttf_novo_valor.value
        index_especificado = self.ttf_index.value
        index_especificado = int(index_especificado)
        self.ltw_lista.controls.insert(
            index_especificado,
            ft.Row(  # Cada elemento da lista é uma Row (linha)
                controls=[  # Cada linha contém dois componentes lado a lado
                    ft.Text(size=20),  # Para o índice da posição atual da lista
                    ft.Text(value=dado_usuario, size=20),  # O dado do usuário
                ]
            ),
        )

    # Função para remover valor em posicao específica
    @preparativos_remocao
    def clk_remover_especifica(self, e):
        index_especificado = self.ttf_index.value
        index_especificado = int(index_especificado)
        self.ltw_lista.controls.pop(index_especificado)  # remover index específico


def main(page: ft.Page):
    App(page)


if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")
