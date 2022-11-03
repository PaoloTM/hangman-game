from random import randint

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
    word = words[randint(1, 171)]
    
    return word

# creacion de un vector donde reemplazamos cada letra de la palabra por un '-'
def hidden_word(word):
    hidden_string = ["_"] * (int(len(word)) - 1)
    
    return hidden_string
        
def hangman_game(word):
    # obtenemos la palabra oculta / convertimos en una lista a nuestra palabra / seteamos una variable score en 0 / seteamos una variable aux vacia / seteamos variable puntos para obtener el maximo de puntos
    hidden_string = hidden_word(word)
    word = list(word)
    score = 0
    aux = ['']
    points = int(len(word)) - 1
    
    # el while se encarga de controlar que el score del jugador no alcance el limite de letras en la palabra que esta dentro de la variable 'points'
    while score < points:
        player_write = input("Ingrese una letra: ")
        
        # recorremos la palabra convertida en lista / comprobamos si la letra que dio el usuario es igual a la letra actual en la palabra y tambien que esa letra no haya sido escrita antes con la variable aux guardamos ese dato / si la letra es igual a la letra en la palabra sumaremos un punto a score / reemplazamos el '-' en la posicion actual por la letra que dio el usuario / guardamos esa letra en la variable aux para que el usuario cuando la vuelva a ingresar sea una letra erronea
        for i in range(len(word)):
            if player_write in word[i] and player_write != aux:
                score += 1
                hidden_string[i] = player_write
                view_string = " ".join(hidden_string)
                # error en el aux deberia ser un array donde guardar las letras y recorrerlo con un for con doble validacion
                aux.append(player_write)
        print(view_string)
    
        
    print("GANASTE!!!!!!!!")

def run():
    words = read_data()
    word = random_word(words)
    
    main_menu()
    
    hidden_word(word)
    print(word)
    
    hangman_game(word)
    
    

if __name__ == '__main__':
    run()