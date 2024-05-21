#from palabras import obtener_palabra
#from diagramas import dibujar_ahorcado

#Palabras

import random

def obtener_palabra():
    palabras = ["python", "programacion", "ordenador", "juego", "ahorcado", "programa"]
    return random.choice(palabras)

#Dibujos

def dibujar_ahorcado(intentos):
    dibujo = [
        """
           -----
           |   |
               |
               |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        ---------
        """
    ]
    return dibujo[intentos]

class Ahorcado:
    def __init__(self):
        self.palabra = obtener_palabra()
        self.letras_adivinadas = []
        self.intentos_restantes = 6

    def mostrar_palabra(self):
        palabra_oculta = ''
        for letra in self.palabra:
            if letra in self.letras_adivinadas:
                palabra_oculta += letra
            else:
                palabra_oculta += '_'
        return palabra_oculta

    def adivinar(self, letra):
        if letra in self.palabra:
            self.letras_adivinadas.append(letra)
        else:
            self.intentos_restantes -= 1
            print(dibujar_ahorcado(6 - self.intentos_restantes))

    def terminar_juego(self):
        if '_' not in self.mostrar_palabra():
            print('¡Felicidades! Has adivinado la palabra:', self.palabra)
            return True
        elif self.intentos_restantes <= 0:
            print('Lo siento, has perdido. La palabra era:', self.palabra)
            return True
        return False

def main():
    juego = Ahorcado()
    print('¡Bienvenido al juego del ahorcado!')
    print('La palabra tiene', len(juego.palabra), 'letras.')
    print(juego.mostrar_palabra())

    while not juego.terminar_juego():
        letra = input('Adivina una letra: ').lower()
        if len(letra) == 1 and letra.isalpha():
            if letra in juego.letras_adivinadas:
                print('Ya has adivinado esa letra. Intenta con otra.')
            else:
                juego.adivinar(letra)
                print(juego.mostrar_palabra())
        else:
            print('Entrada inválida. Por favor, introduce una sola letra.')

if __name__ == "__main__":
    main()
