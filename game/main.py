import time
import sys
import os
import random

# Funcion para validar si son numeros lo que se ingresa.


def validar_numero(text, text2):
    while True:
        try:
            delay_print(text)
            valor = int(input("\n=> "))
        except ValueError:
            delay_print(f"Invalid option\nPlease only enter numbers{text2}\n")
            time.sleep(1.5)
            os.system("cls")
            title()
            continue
        return valor
    
# Funcion para escribir letra por letra


def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.02)  # Tiempo de espera estre cada letra


def resultado_del_juego(resultado):
    time.sleep(0.5)
    os.system("cls")
    title()
    delay_print(
        f"You chose {options[user_option]} Computer chose {options[computer_option]}\n{resultado}\n")
    time.sleep(2)


def repetir(text):
    while True:
        repetir = validar_numero(f"Play again?\n1-Yes  2-No", text)
        if repetir == 2:
            global ciclo
            delay_print("Thanks for playing, see you next time!")
            ciclo = 0
            return ciclo
        elif repetir == 1:
            return os.system("cls")
        else:
            delay_print(f"Invalid option\nPlease only enter numbers{text}\n")
            time.sleep(1.5)
            os.system("cls")
            title()


def title():
    print("______           _     ______                             _____      _                         ")
    print("| ___ \         | |    | ___ \                           /  ___|    (_)                        ")
    print("| |_/ /___   ___| | __ | |_/ /_ _ _ __  _ __   ___ _ __  \ `--.  ___ _ ___ ___  ___  _ __ ___  ")
    print("|    // _ \ / __| |/ / |  __/ _` | '_ \| '_ \ / _ \ '__|  `--. \/ __| / __/ __|/ _ \| '__/ __| ")
    print("| |\ \ (_) | (__|   <  | | | (_| | |_) | |_) |  __/ |    /\__/ / (__| \__ \__ \ (_) | |  \__ \ ")
    print("\_| \_\___/ \___|_|\_\ \_|  \__,_| .__/| .__/ \___|_|    \____/ \___|_|___/___/\___/|_|  |___/ ")
    print("                                 | |   | |           Score                                     ")
    print(
        f"                                 |_|   |_|      you {score[0]} Computer {score[1]}            ")


score = [0, 0]
options = ("", "Rock \U0001f44a", "Paper \u270B", "Scissor\u2702\ufe0f ")
#          0      1                  2                3
ciclo = 1

while ciclo == 1:
    os.system("cls")
    title()
    user_option = validar_numero(
        "Enter a choice\n1 Rock\U0001f44a\n2 Paper\u270B\n3 Scissor\u2702\ufe0f \n4 Exit.", " between 1 and 4.")
    if user_option not in (1, 2, 3, 4):
        delay_print(
            "Invalid option\nPlease only enter numbers between 1 and 4\n")
        time.sleep(1.5)
    if user_option == 4:
        time.sleep(0.5)
        ciclo = 0
        delay_print("Thanks for playing, see you next time!")
    computer_option = random.randint(1, 3)
    if user_option == computer_option:
        resultado_del_juego("It's a tie!")
        repetir(" between 1 and 2.")
    elif user_option == 1 and computer_option == 2 or user_option == 2 and computer_option == 3 or user_option == 3 and computer_option == 1:
        resultado_del_juego("You lose")
        score[1] += 1
        repetir(" between 1 and 2.")
    elif user_option == 1 and computer_option == 3 or user_option == 2 and computer_option == 1 or user_option == 3 and computer_option == 2:
        resultado_del_juego("You win!")
        score[0] += 1
        repetir(" between 1 and 2.")