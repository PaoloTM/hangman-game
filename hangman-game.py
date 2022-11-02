from random import randint

def read_data():
    words = []
    
    with open("./data.txt", "r", encoding="utf-8") as f:
        for lines in f:
            words.append(lines)
            
    return words

def random_word(words):
    word = words[randint(1, 171)]
    
    return word

def hidden_word(word):
    hidden_string = ["_"] * (int(len(word)) - 1)
    
    return hidden_string
        
def hangman_game(word):
    hidden_string = hidden_word(word)
    word = list(word)
    score = 0
    points = int(len(word)) - 1
    while score < points:
        player_write = input("Ingrese una letra: ")
        for i in range(len(word)):
            # while player_write in word[i]:
            #     pass
            if player_write in word[i]:
                score += 1
                hidden_string[i] = player_write
                view_string = " ".join(hidden_string) 
                print(view_string)
            # else:
            #     view_string = " ".join(hidden_string) 
            #     print(view_string)
    
        
    print("GANASTE!!!!!!!!")

def run():
    words = read_data()
    word = random_word(words)
    
    hidden_word(word)
    print(word)
    
    hangman_game(word)
    
    

if __name__ == '__main__':
    run()