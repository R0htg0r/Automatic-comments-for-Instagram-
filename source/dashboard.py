from colorama import Fore, Back, Style, init
import pyautogui
import time
import os

os.system("mode 120, 30")

class Poxtrop():
    def __init__(cuspida):
        cuspida.settings()

    def interface(cuspida):
        init()
        print(Fore.YELLOW + """
       #########        ######     ##        ##   ###########       #######         ######       #########
        ##     ##      ##    ##    ##        ##  ##   ###   ##     ##     ##       ##    ##       ##     ##
        ##      ##    ##      ##   ##        ##       ###         ##       ##     ##      ##      ##      ##
        ##      ##    ##      ##   ##        ##       ###        ##               ##      ##      ##      ##
        ##     ##     ##      ##   ############       ###        ##               ##      ##      ##     ##
        ########      ##      ##   ############       ###        ##               ##      ##      ########
        ##    ##      ##      ##   ##        ##       ###        ##     #######   ##      ##      ##    ##
        ##     ##     ##      ##   ##        ##       ###         ##       ##     ##      ##      ##     ##
        ##      ##     ##    ##    ##        ##       ###          ##     ##       ##    ##       ##      ##
       ##        ##     ######     ##        ##      #####          #######         ######       ##        ##""")
        print(Fore.GREEN + """
        Informações:
            1) Coloque um comentário simples, e pequeno.
            2) Defina o tempo em segundos, o recomendado é 10s

        Versão: 1.0
        """)

    def settings(cuspida):
        cuspida.interface()
        try:
            button_message = input(Fore.WHITE + " Comentário: ")
            if button_message == "":
                pass
            button_tempo = int(input(Fore.WHITE + " Segundos: "))
            button_clicked = 0
            os.system("cls")
            cuspida.interface()
            print(Fore.YELLOW + " Sua caixa de transporte: ")

            while True:
                button_clicked += 1
                time.sleep(button_tempo)
                button_chatImg = pyautogui.locateOnScreen('./img/chat.png')
                button_location = pyautogui.center(button_chatImg)
                pyautogui.click(button_location)

                pyautogui.typewrite(button_message)
                pyautogui.press("enter")

                print(Fore.GREEN + f"  {button_clicked}ª mensagem enviada com sucesso. ")
        except(ValueError):
            exit()
        except(TypeError):
            exit()
        except(KeyboardInterrupt):
            exit()
Poxtrop()
