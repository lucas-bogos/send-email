import smtplib
import PySimpleGUI as sg
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Interface:
    def __init__(self):
        sg.theme('DarkPurple4')
        layout = [
            [sg.Text('Servidor ', size=(8,1)),
                sg.Input(key='_using_server_', size=(21, 1))],
            [sg.Text('De ', size=(8,1)), 
                sg.Input(key='_from_', size=(21,1))], 
            [sg.Text('Para ', size=(8,1)),
                sg.Input(key='_to_', size=(21,1))],
            [sg.Text('Assunto ', size=(8,1)),
                sg.Input(key='_matter_', size=(21,1))],
            [sg.Text('Mensagem ', size=(8,1)),
                sg.Input(key='_message_', size=(21,2))],
            [sg.Text('Logs')],
            [sg.Output(size=(31, 5))],
            [sg.Button('Enviar')]
        ]
        self.windowMain = sg.Window('SendEmail 1.0', layout, icon='Blackvariant-Shadow135-System-Mail.ico')

    def Home(self):
        while True:
            event, values = self.windowMain.read()
            if event == sg.WINDOW_CLOSED:
                break
            if event == 'Enviar':
                self.configs(values['_using_server_'], values['_from_'], values['_to_'], values['_matter_'], values['_message_'])

    def configs(self, _using_server_, _from_, _to_, _matter_, _message_):
        try:
            Select = _using_server_
            s = 'smtp.{}.com'.format(Select)
            server = smtplib.SMTP(s, 587)
            server.starttls()
            print('Configurando o server...')

            #email_from = input(str('De: '))
            print('Fazendo o login, aguarde...')
            server.login(_from_, open('senha.txt').read().strip())
            #email_to = input(str('Para: '))
            #subject = input(str('Assunto: '))

            msg = MIMEMultipart()
            msg['From'] = _from_
            msg['To'] = _to_
            msg['Subject'] = _matter_

            #message = input(str('Mensagem: '))
            msg.attach(MIMEText(_message_, 'plain'))
            text = msg.as_string()
            print('Enviando a mensagem...')
            #SET
            server.sendmail(_from_, _to_, text)
            server.quit()
            print('Sucesso ao enviar o email') 
        except:
            print('Ops, ocorreu um erro :(')
        
debg = Interface()
debg.Home()       