import random  # 1. Importamos a biblioteca para gerar aleatoriedade

def hangman(): # Removi o parâmetro 'word' para a função escolher sozinha
    # 2. Nossa lista de palavras possíveis
    word_list = ["python", "algoritmo", "computador", "programacao", "cat"]
    
    # 3. O random.choice escolhe um item aleatório da lista
    word = random.choice(word_list)
    
    wrong = 0
    stages = ["",
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
             ]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    
    print("Bem-vindo ao jogo!")
    
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Adivinhe uma letra: "
        char = input(msg).lower() # .lower() garante que 'A' ou 'a' funcionem
        
        if char in rletters:
            # Lógica para quando a letra aparece mais de uma vez
            while char in rletters:
                cind = rletters.index(char)
                board[cind] = char
                rletters[cind] = '$'
        else:
            wrong += 1
        
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))
        
        if "__" not in board:
            print("Victory! !")
            print("A palavra era: " + word)
            win = True
            break
            
    if not win:
        print("\n".join(stages[0: wrong]))
        print("You lose! A palavra era {}.".format(word))

# Agora basta chamar a função sem passar nada

hangman()
