import flet as ft


def main(page: ft.Page):
    # Configurar tema de cor da page
    page.theme_mode = ft.ThemeMode.LIGHT
    # Setar largura da page
    page.window.width = 400
    # Setar altura da page
    page.window.height = 680
    # Manter App sobre outros aplicativos
    page.window.always_on_top = True

    # Título da aplicação
    txt_titulo = ft.Text(value="Lista Encadeada Simples", size=28)

    # Criar uma lista em FLET
    ltw_lista = ft.ListView(expand=1, auto_scroll=True)

    # Comprimento da lista
    txt_comprimento = ft.Text(value="Comprimento: ", size=23)

    # Texto digitado para inserir na lista
    ttf_texto = ft.TextField()

    # Função para recontar os índices da lista
    def recontar_indices():
        i = 0  # Contador inciando em zero
        # Para cada elemento da lista
        for elemento in ltw_lista.controls:
            # Atribua o atual valor da variável i
            elemento.controls[0].value = i
            # Incremente com mais 1 o valor da variável i
            i += 1

    # Função para inserir valor no final da lista
    def clk_inserir_final(e):
        # Obter valor digitado pelo usuário
        valor = ttf_texto.value
        # Limpar a caixa de texto
        ttf_texto.value = ""
        # Inserir valor no final da lista
        ltw_lista.controls.append(
            # Cada elemento da lista é uma Row (linha)
            ft.Row(
                # Cada linha contém dois componentes lado a lado
                controls=[
                    # Primeiro componente contém o índice da posição atual da lista
                    # ft.Text(value=len(ltw_lista.controls), size=20),
                    ft.Text(size=20),
                    # Segundo componente contém o valor digitado pelo usuário
                    ft.Text(value=valor, size=20),
                ]
            )
        )
        # Atualiza a informação de comprimento da lista
        txt_comprimento.value = f"Comprimento: {len(ltw_lista.controls)}"
        # Invocação da função para recontar os índices da lista
        recontar_indices()
        # Atualizar a página toda
        page.update()

    # Botão para inserir valor no final da lista
    btn_inserir_final = ft.ElevatedButton(
        text="Inserir final", on_click=clk_inserir_final
    )

    # Função para inserir valor no início da lista
    def clk_inserir_inicio(e):
        # Obter texto digitado pelo usuário
        valor = ttf_texto.value
        # Limpar a caixa de texto
        ttf_texto.value = ""
        # Criar uma Row (linha) com índice e novo valor
        lista_aux = ft.Row(
            controls=[ft.Text(value="", size=20), ft.Text(value=valor, size=20)]
        )
        # Criar uma linha com uma lista com o novo valor
        lista_aux = [lista_aux]
        # Inserir novo valor no inicio da lista usando o operador de adição
        ltw_lista.controls = lista_aux + ltw_lista.controls
        # Atualizar a informação de comprimento da lista
        txt_comprimento.value = f"Comprimento: {len(ltw_lista.controls)}"
        # Invocação da função para recontar os índices da lista
        recontar_indices()
        # Atualizar a página toda
        page.update()

    # Botão para inserir valor no início da lista
    btn_inserir_inicio = ft.ElevatedButton(
        text="Inserir inicio", on_click=clk_inserir_inicio
    )

    # Função para remover valor no final da lista
    def clk_remover_inicio(e):
        # remover texto no inicio da lista
        ltw_lista.controls.pop(0)
        # Atualizar a informação de comprimento da lista
        txt_comprimento.value = f"Comprimento: {len(ltw_lista.controls)}"
        # Invocação da função para recontar os índices da lista
        recontar_indices()
        # Atualizar a página toda
        page.update()

    # Botão para remover valor no inicio da lista
    btn_remover_inicio = ft.ElevatedButton(
        text="Remover inicio", on_click=clk_remover_inicio
    )

    # Função para remover valor no final da lista
    def clk_remover_final(e):
        # remover texto no final da lista
        ltw_lista.controls.pop()
        # Atualizar a informação de comprimento da lista
        txt_comprimento.value = f"Comprimento: {len(ltw_lista.controls)}"
        # Invocação da função para recontar os índices da lista
        recontar_indices()
        # Atualizar a página toda
        page.update()

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

    # Atualizar/Recarregar a page
    page.update()


ft.app(main)
