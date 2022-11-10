from random import randint
import os

# --- Limpiar pantalla ---
def clean_screen():
    os.system("cls")

# --- Main menu ---
def main_menu():
    print("""
     ██╗░░██╗░█████╗░███╗░░██╗░██████╗░███╗░░░███╗░█████╗░███╗░░██╗  ░░░░░░  ░██████╗░░█████╗░███╗░░░███╗███████╗
     ██║░░██║██╔══██╗████╗░██║██╔════╝░████╗░████║██╔══██╗████╗░██║  ░░░░░░  ██╔════╝░██╔══██╗████╗░████║██╔════╝
     ███████║███████║██╔██╗██║██║░░██╗░██╔████╔██║███████║██╔██╗██║  █████╗  ██║░░██╗░███████║██╔████╔██║█████╗░░
     ██╔══██║██╔══██║██║╚████║██║░░╚██╗██║╚██╔╝██║██╔══██║██║╚████║  ╚════╝  ██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░
     ██║░░██║██║░░██║██║░╚███║╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║  ░░░░░░  ╚██████╔╝██║░░██║██║░╚═╝░██║███████╗
     ╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝  ░░░░░░  ░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝""")
    print("""
          
▄█ ▄▄   █▀█ █░░ ▄▀█ █▄█     ░░▄▀ ░░▄▀     ▀█ ▄▄   █▀▀ ▀▄▀ █ ▀█▀
░█ ░░   █▀▀ █▄▄ █▀█ ░█░     ▄▀░░ ▄▀░░     █▄ ░░   ██▄ █░█ █ ░█░
          """)   

# lectura de datos a utilizar
def read_data():
    words = []
    
    with open("./data.txt", "r", encoding="utf-8") as f:
        for lines in f:
            words.append(lines)
            
    return words

# seleccion de una palabra al azar
def random_word(words):
    word = words[randint(0, 170)]
    
    return word

# Reemplazamos las vocales con acentos a sin acento, para evitar errores de tipeo
def delete_accent(word):
    word = list(word)
    letter_accent = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u")
    ) 
    for i in range(len(word)):
        for a, b in letter_accent:
            if word[i] == a:
                word[i] = b
    
    return word

# creacion de un vector donde reemplazamos cada letra de la palabra por un '-'
def hidden_word(word):
    hidden_string = ["_"] * (int(len(word)) - 1)
    
    return hidden_string

# texto de ganaste
def winner():
    print("""
░██████╗░░█████╗░███╗░░██╗░█████╗░░██████╗████████╗███████╗  ██╗██████╗░
██╔════╝░██╔══██╗████╗░██║██╔══██╗██╔════╝╚══██╔══╝██╔════╝  ╚═╝██╔══██╗
██║░░██╗░███████║██╔██╗██║███████║╚█████╗░░░░██║░░░█████╗░░  ░░░██║░░██║
██║░░╚██╗██╔══██║██║╚████║██╔══██║░╚═══██╗░░░██║░░░██╔══╝░░  ░░░██║░░██║
╚██████╔╝██║░░██║██║░╚███║██║░░██║██████╔╝░░░██║░░░███████╗  ██╗██████╔╝
░╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░╚══════╝  ╚═╝╚═════╝░""")

# texto de perdiste
def loss():
    print("""
██████╗░███████╗██████╗░██████╗░██╗░██████╗████████╗███████╗  ██╗░░██╗
██╔══██╗██╔════╝██╔══██╗██╔══██╗██║██╔════╝╚══██╔══╝██╔════╝  ╚═╝░██╔╝
██████╔╝█████╗░░██████╔╝██║░░██║██║╚█████╗░░░░██║░░░█████╗░░  ░░░██╔╝░
██╔═══╝░██╔══╝░░██╔══██╗██║░░██║██║░╚═══██╗░░░██║░░░██╔══╝░░  ░░░╚██╗░
██║░░░░░███████╗██║░░██║██████╔╝██║██████╔╝░░░██║░░░███████╗  ██╗░╚██╗
╚═╝░░░░░╚══════╝╚═╝░░╚═╝╚═════╝░╚═╝╚═════╝░░░░╚═╝░░░╚══════╝  ╚═╝░░╚═╝""")

# seteamos el vector para mostrar la imagen del ahorcado
def pic_hangman():
    hangman_pic = ["""  +---+
  |   |
      |
      |
      |
      |
=========""", """  +---+
  |   |
  O   |
      |
      |
      |
=========""", """  +---+
  |   |
  O   |
  |   |
      |
      |
=========""", """  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""", """  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""", """  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""", """  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========="""]
    return hangman_pic

# verifica que tenga al menos 1 punto de perdida para mostrar la imagen del ahorcado
def verified_loss_point(score_loss, view_hangman):
    if score_loss > 0:
        print(view_hangman)
        
def hangman_game(word):
    # seteamos el vector que nos dibuja al ahorcado por cada falla
    hangman_pic = pic_hangman()
    # obtenemos la palabra oculta / convertimos en una lista a nuestra palabra / seteamos una variable score en 0 / seteamos una variable aux vacia / seteamos variable puntos para obtener el maximo de puntos
    hidden_string = hidden_word(word)
    # word = list(word) // los seteamos en delete_accent
    score_win = 0
    score_loss = 0
    score_verified = 0
    aux = ['']
    points = int(len(word)) - 1
    # seteamos la palabra oculta para mostrarsela al usuario
    view_string = " ".join( hidden_string)
    # seteamos la imagen del ahorcado
    view_hangman = "".join(hangman_pic[0])
    
    # el while se encarga de controlar que el score del jugador no alcance el limite de letras en la palabra que esta dentro de la variable 'points'
    while score_win < points:
        clean_screen()
        print(word) # muestra la palabra oculta (solo para test xd) 
        verified_loss_point(score_loss, view_hangman)
        print(view_string)
        player_write = input("Ingrese una letra: ").lower()
        
        # comprobamos que la letra no haya sido ingresada anteriormente
        while (player_write in aux) or (len(player_write) > 1):
            clean_screen()
            verified_loss_point(score_loss, view_hangman)
            print(view_string)
            player_write = input("Ingrese una letra valida: ").lower()
        
        # recorremos la palabra convertida en lista / comprobamos si la letra que dio el usuario es igual a la letra actual en la palabra y tambien que esa letra no haya sido escrita antes con la variable aux guardamos ese dato / si la letra es igual a la letra en la palabra sumaremos un punto a score / reemplazamos el '-' en la posicion actual por la letra que dio el usuario / guardamos esa letra en la variable aux para que el usuario cuando la vuelva a ingresar sea una letra erronea
        for i in range(len(word)):
            if player_write == word[i]:
                score_win += 1
                hidden_string[i] = player_write
                view_string = " ".join(hidden_string)
                aux.append(player_write)
        
        if score_win == score_verified:
            score_loss += 1
            view_hangman = "".join(hangman_pic[score_loss - 1])
            print(view_hangman)
            print(view_string)
                
        elif score_win > 1:
            clean_screen()
            verified_loss_point(score_loss, view_hangman)
            print(view_string)
        
        if score_loss > 6:
            clean_screen()
            print(view_hangman)
            loss()
            break
        
        if score_win == points:
            clean_screen()
            verified_loss_point(score_loss, view_hangman)
            winner()
            break
        
        score_verified = score_win
        
        

    print("\n")
    input("PRESIONA ENTER PARA CONTINUAR: ")

def run():
    clean_screen()
    main_menu()
    play = 0
    
    while play != 2:
        if play == 1:
            clean_screen()
            words = read_data()
            word = random_word(words)
            word = delete_accent(word)
            print(word)
            hangman_game(word)
            clean_screen()
            main_menu()
        try:
            play = int(input("seleccione una opcion: "))
        except:
            clean_screen()
            main_menu()
            print("Ingrese una opcion valida")
    
    clean_screen()
    exit()
    

if __name__ == '__main__':
    run()