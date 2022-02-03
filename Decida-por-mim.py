# Projeto 2 - Decida por mim
# Resposta automatica aleatoria
import random
import PySimpleGUI as sg

class DecidaPorMim:
    def __init__(self):
        self.respostas = [
            'Sempre siga em frente!',
            'Quando você menos espera acontecerá!',
            'Acho uma boa ideia!',
            'Não sei, você que sabe',
            'Será ? Vai que da certo!'
            'Não faz isso Não!',
            'Acho que não tá na hora certa!'
        ]

    def Iniciar(self):

        layout = [
            [sg.Text('Faça sua pergunta:')],
            [sg.Input()],
            [sg.Output(size=(50, 10))],
            [sg.Button('Decida por mim')]
        ]

        self.janela = sg.Window('Decida por Mim!', layout=layout)
        while True:

            self.eventos, self.valores = self.janela.Read()

            if self.eventos == 'Decida por mim':
                print(random.choice(self.respostas))


decida = DecidaPorMim()
decida.Iniciar()
