import flet as ft  # Importar biblioteca do flet
from flet import colors
from decimal import Decimal

botoes = [  # Criar uma lista-dicionário para os botões, como nome, cor_text e de fundo
    {'nome': 'AC', 'cor': colors.BLACK, 'fundo': colors.GREEN},
    {'nome': '+-', 'cor': colors.BLACK, 'fundo': colors.BLUE},
    {'nome': '%', 'cor': colors.BLACK, 'fundo': colors.BLUE},
    {'nome': '/', 'cor': colors.BLACK, 'fundo': colors.BLUE},
    {'nome': '7', 'cor': colors.WHITE, 'fundo': colors.AMBER_300},
    {'nome': '8', 'cor': colors.WHITE, 'fundo': colors.AMBER_300},
    {'nome': '9', 'cor': colors.WHITE, 'fundo': colors.AMBER_300},
    {'nome': 'X', 'cor': colors.BLACK, 'fundo': colors.BLUE},
    {'nome': '4', 'cor': colors.WHITE, 'fundo': colors.AMBER_300},
    {'nome': '5', 'cor': colors.WHITE, 'fundo': colors.AMBER_300},
    {'nome': '6', 'cor': colors.WHITE, 'fundo': colors.AMBER_300},
    {'nome': '+', 'cor': colors.BLACK, 'fundo': colors.BLUE},
    {'nome': '1', 'cor': colors.WHITE, 'fundo': colors.AMBER_300},
    {'nome': '2', 'cor': colors.WHITE, 'fundo': colors.AMBER_300},
    {'nome': '3', 'cor': colors.WHITE, 'fundo': colors.AMBER_300},
    {'nome': '-', 'cor': colors.BLACK, 'fundo': colors.BLUE},
    {'nome': '0', 'cor': colors.WHITE, 'fundo': colors.AMBER_300},
    {'nome': ',', 'cor': colors.BLACK, 'fundo': colors.AMBER_300},
    {'nome': '=', 'cor': colors.BLACK, 'fundo': colors.BLUE}
]


def main(page: ft.Page):  # definir uma função com nome main e imprtar uma bibliot do flet chamada page
    page.bgcolor = '#000'  # código HEX para preto
    page.window_resizable = False  # Para que a janela não possa ser redimensionada
    page.window_width = 325
    page.window_height = 450
    page.title = 'Calculadora'
    page.window_always_on_top = True

    # Cria a fnção resultado com as definições gráficas
    result = ft.Text(value='0', color=colors.WHITE, size=20)

    def calculate(nome, value_at):
        try:
            value = eval(value_at)

            if nome == '%':
                value /= 100
            elif nome == '+-':
                value = -value
        except:
            return 'Error'

        digits = min(abs(Decimal(value).as_tuple().exponent), 5)
        return format(value, f'.{digits}f')

    def select(e):
        # Se o valor, botão clicado, for diferente de zero é executado, caso contrario permanece sem mudar
        value_at = result.value if result.value not in ('0', 'Error') else ''
        value = e.control.content.value

        if value.isdigit():  # Se o valor for um dígito ele vai agregar um ao outro Ex.: 78 e não 7 8
            value = value_at + value
        elif value == 'AC':  # Se o botão for AC ele zera a conta
            value = '0'
        else:
            # Se ele for um valor e se o digitado for uma operação matemática
            if value_at and value_at[-1] in ('/', 'X', '+', '-', ','):
                # Nessa condição ele será igual a ele mesmo menos o ultimo elemento digitado
                value_at = value_at[:-1]

            value = value_at + value

            if value[-1] in ('=', '%', '+-'):
                # Criar a função calculate
                value = calculate(nome=value[-1], value_at=result.value)

        result.value = value
        result.update()

    display = ft.Row(  # Cria a função display: Uma caixa alinhada à direita para exibir resultado/operações
        width=300,
        controls=[result],
        alignment='end'
    )

    btn = [ft.Container(
        content=ft.Text(value=btn['nome'], color=btn['cor']),
        width=60,
        height=60,
        bgcolor=btn['fundo'],
        border_radius=100,
        alignment=ft.alignment.center,
        on_click=select  # Quando clicado ele chama a função 'select' criada posteriormente
    ) for btn in botoes]

    keyboard = ft.Row(
        width=325,
        wrap=True,  # Gera quebra de linha quando chegar no fim da janela do app
        controls=btn,
        alignment='end'
    )

    page.add(display, keyboard)


ft.app(target=main)
