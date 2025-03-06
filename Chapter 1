import numpy as np
import random

def choose_next_state(P, current_state):
    """Selecciona el próximo estado basado en la matriz de transición."""
    return np.random.choice(len(P), p=P[current_state])

def play_game():
    """Juego interactivo basado en un proceso de Markov."""
    rooms = ["Entrada", "Pasillo", "Biblioteca", "Sótano", "Salida"]
    P = np.array([[0.2, 0.5, 0.3, 0.0, 0.0],  # Entrada
                  [0.1, 0.4, 0.3, 0.2, 0.0],  # Pasillo
                  [0.2, 0.2, 0.3, 0.3, 0.0],  # Biblioteca
                  [0.1, 0.3, 0.2, 0.2, 0.2],  # Sótano
                  [0.0, 0.0, 0.0, 0.0, 1.0]]) # Salida (estado absorbente)
    
    current_state = 0  # Comienza en la Entrada
    steps = 0
    
    print("¡Bienvenido a la Casa Encantada!")
    print("Tu objetivo es llegar a la Salida.")
    
    while current_state != 4:
        print(f"Estás en {rooms[current_state]}")
        input("Presiona Enter para moverte...")
        current_state = choose_next_state(P, current_state)
        steps += 1
    
    print(f"¡Has escapado en {steps} pasos! ¡Felicidades!")

if __name__ == "__main__":
    play_game()
