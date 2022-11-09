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
# ERROR FALTA VERIFICAR COMO UTILIZAR LAS TUPLAS Y COMO REEMPLAZAR EL VALOR A POR EL B
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
        
def hangman_game(word):
    # obtenemos la palabra oculta / convertimos en una lista a nuestra palabra / seteamos una variable score en 0 / seteamos una variable aux vacia / seteamos variable puntos para obtener el maximo de puntos
    hidden_string = hidden_word(word)
    # word = list(word)
    score = 0
    aux = ['']
    points = int(len(word)) - 1
    
    # el while se encarga de controlar que el score del jugador no alcance el limite de letras en la palabra que esta dentro de la variable 'points'
    while score < points:
        player_write = input("Ingrese una letra: ").lower()
        
        # comprobamos que la letra no haya sido ingresada anteriormente
        while player_write in aux:
            player_write = input("Ingrese otra letra, no repetida: ").lower()
        
        # recorremos la palabra convertida en lista / comprobamos si la letra que dio el usuario es igual a la letra actual en la palabra y tambien que esa letra no haya sido escrita antes con la variable aux guardamos ese dato / si la letra es igual a la letra en la palabra sumaremos un punto a score / reemplazamos el '-' en la posicion actual por la letra que dio el usuario / guardamos esa letra en la variable aux para que el usuario cuando la vuelva a ingresar sea una letra erronea
        for i in range(len(word)):
            if player_write == word[i]:
                score += 1
                hidden_string[i] = player_write
                view_string = " ".join(hidden_string)
                aux.append(player_write)
        if score > 0:
            print(view_string)
        else:
            continue
    
        
    print("GANASTE!!!!!!!!")

def run():
    clean_screen()
    main_menu()
    
    play = int(input())
    
    while play == 1:
        clean_screen()
        words = read_data()
        word = random_word(words)
        word = delete_accent(word)
        print(word)
        hangman_game(word)
        clean_screen()
        main_menu()
        play = int(input())
    
    if play == 2:
        clean_screen()
        exit()
    
    

if __name__ == '__main__':
    run()