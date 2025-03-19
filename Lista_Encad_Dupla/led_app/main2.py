import flet as ft


def main(page: ft.Page):

    page.theme_mode = ft.ThemeMode.LIGHT  # Configurar tema de cor da page
    page.window.width = 400  # Setar largura da page
    page.window.height = 680  # Setar altura da page
    page.window.always_on_top = True  # Manter App sobre outros aplicativos
    page.window.left = 750

    txt_titulo = ft.Text(value="Lista Encadeada Simples", size=28)  # Título do app
    ltw_lista = ft.ListView(expand=1, auto_scroll=True)  # Criar uma lista em FLET
    txt_comprimento = ft.Text(value="Comprimento: ", size=23)  # Comprimento da lista
    ttf_texto = ft.TextField()  # Texto digitado para inserir na lista

    # Função para obter dado do usuário
    def obter_dado_usuario() -> str:
        dado_usuario = ttf_texto.value  # Obter dado do usuário
        ttf_texto.value = ""  # Limpar campo de obtenção de dado do usuário
        ttf_texto.focus()  # Atribuir foco ao componente ttf_texto
        ttf_texto.update()  # Atualiza estado do componente
        return dado_usuario  # Retornar dado do usuário

    # Função para recontar os índices da lista
    def recontar_indices():
        i = 0  # Contador inciando em zero
        for elemento in ltw_lista.controls:  # Para cada elemento da lista
            elemento.controls[0].value = i  # Atribua o atual valor da variável i
            i += 1  # Incremente com mais 1 o valor da variável i
        txt_comprimento.value = f"Comprimento: {i}"  # Atualiza comprimento da lista
        txt_comprimento.update()  # Atualiza estado do componente

    # Função decoradora para insercoes
    def preparativos_insercao(func):
        def wrapper(*args, **kwargs):
            dado_usuario = obter_dado_usuario()
            func(dado_usuario=dado_usuario, *args, **kwargs)
            recontar_indices()
            ltw_lista.update()  # Atualiza estado do componente

        return wrapper

    # Função para inserir valor no final da lista
    @preparativos_insercao
    def clk_inserir_final(e, dado_usuario):
        ltw_lista.controls.append(  # Inserir dado_usuario no final da lista
            ft.Row(  # Cada elemento da lista é uma Row (linha)
                controls=[  # Cada linha contém dois componentes lado a lado
                    ft.Text(size=20),  # Para o índice da posição atual da lista
                    ft.Text(value=dado_usuario, size=20),  # O dado do usuário
                ]
            )
        )

    # Botão para inserir valor no final da lista
    btn_inserir_final = ft.ElevatedButton(
        text="Inserir final", on_click=clk_inserir_final
    )

    # Função para inserir dado_usuario no início da lista
    @preparativos_insercao
    def clk_inserir_inicio(e, dado_usuario):
        # Criar uma Row (linha) com índice e novo dado_usuario
        nova_linha = ft.Row(
            controls=[ft.Text(value="", size=20), ft.Text(value=dado_usuario, size=20)]
        )
        lista_aux = [nova_linha]  # Criar uma lista com a nova linha
        ltw_lista.controls = lista_aux + ltw_lista.controls  # Juntar as listas

    # Botão para inserir valor no início da lista
    btn_inserir_inicio = ft.ElevatedButton(
        text="Inserir inicio", on_click=clk_inserir_inicio
    )

    # Função decorada para remocoes
    def preparativos_remocao(func):
        def wrapper(*args, **kwargs):
            func(*args, **kwargs)
            txt_comprimento.value = f"Comprimento: {len(ltw_lista.controls)}"
            ttf_texto.focus()  # Atribuir foco ao componente ttf_texto
            recontar_indices()  # Recontar os índices da lista
            txt_comprimento.update()  # Atualiza estado do componente
            ltw_lista.update()  # Atualiza estado do componente

        return wrapper

    # Função para remover valor no final da lista
    @preparativos_remocao
    def clk_remover_inicio(e):
        ltw_lista.controls.pop(0)  # remover texto no inicio da lista

    # Botão para remover valor no inicio da lista
    btn_remover_inicio = ft.ElevatedButton(
        text="Remover inicio", on_click=clk_remover_inicio
    )

    # Função para remover valor no final da lista
    @preparativos_remocao
    def clk_remover_final(e):
        ltw_lista.controls.pop()  # remover texto no final da lista

    # Botão para remover valor no final da lista
    btn_remover_final = ft.ElevatedButton(
        text="Remover final", on_click=clk_remover_final
    )

    # Criar linha para alinhar botões
    linha = ft.Row(
        wrap=True,
        controls=[
            btn_inserir_inicio,
            btn_inserir_final,
            btn_remover_inicio,
            btn_remover_final,
        ],
    )

    page.add(
        txt_titulo,
        txt_comprimento,
        ltw_lista,
        ttf_texto,
        linha,
    )
    ttf_texto.focus()  # Atribuir foco ao componente ttf_texto

    page.update()  # Atualizar/Recarregar a page


if __name__ == "__main__":
    ft.app(main)
