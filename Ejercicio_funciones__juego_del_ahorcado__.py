import random

# Lista de palabras predefinidas
word = ["python", "programacion", "tecnologia", "computadora", "inteligencia", "datos"]

# Función para seleccionar una palabra al azar
def choise_word():
    return random.choice(word)

# Función para mostrar el tablero actual
def show_board(word, guessed_letter):
    board = ""
    for letter in word:
        if letter in guessed_letter:
            board += letter
        else:
            board += "_"
    return board

# Función principal del juego
def play_ahorcado():
    secret_word = choise_word()
    max_tries = 5
    guessed_letter = []
    
    print("¡Bienvenido al juego del ahorcado!")
    print("Tienes {} intentos para adivinar la palabra.".format(max_tries))
    
    while max_tries > 0:
        actual_board = show_board(secret_word, guessed_letter)
        print("\nPalabra a adivinar: " + actual_board)
        letter = input("Ingresa una letra: ").lower()
        
        if len(letter) != 1 or not letter.isalpha():
            print("Por favor, ingresa una sola letra válida.")
            continue
        
        if letter in guessed_letter :
            print("Ya has adivinado esta letra.")
            continue
        
        guessed_letter.append(letter)
        
        if letter in secret_word:
            print("¡Adivinaste una letra correctamente!")
        else:
            max_tries -= 1
            print("Letra incorrecta, te quedan {} intentos.".format(max_tries))

        if all(letter in guessed_letter for letter in secret_word):
            print("¡Felicidades! Has adivinado la palabra: {}".format(secret_word))
            break
        
    
    if max_tries == 0:
        print("\n¡Has perdido! La palabra secreta era: {}".format(secret_word))

# Iniciar el juego
if __name__ == "__main__":
    play_ahorcado()