# Simulador de DADO
# Simular o uso de um DADO, gerando um valor de 1 até 6
import random
import PySimpleGUI as sg


class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        # Layout
        self.layout = [
            [sg.Text('Jogar DADO ?')],
            [sg.Button('sim'), sg.Button('Não')]
        ]

    def Iniciar(self):
        # criar uma janela
        self.janela = sg.Window('Simulador de Dado', layout=self.layout)  # ler os valores da tela
        self.eventos, self.valores = self.janela.Read()   # fazer alguma coisa com esses valores

        try:
            if self.eventos == 'sim' or self.eventos == 's':
                self.GerarValorDoDado()
            elif self.eventos == 'Não' or self.eventos == 'n':
                print('Obrigado por participar.')
            else:
                print('Digitar sim ou não')
        except:
            print('Resposta invalida.')

    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))


simulador = SimuladorDeDado()
simulador.Iniciar()



