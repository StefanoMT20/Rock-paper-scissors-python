import random
numero_aleatorio = random.randint(1,3)
 

menu = """
    ¡Vamos a jugar Piedra, papel o tijera..... CON LA PC!
    Te explico como va la cosa, la pc escogerá el número optimo para vencerte
    TU RETO ES GANARLE A UNA PC EN UN SIMPLE JUEGO TRADICIONAL O... ¿NO PUEDES HACERLO?
    ¡QUE EMPIECE EL RETO, ESCOJE UNA OPCION DEL 1 AL 3!
   
   
         1 - Papel
         2 - Piedra
         3 - Tijera
    
    ------>""" 
numero_elegido = int(input(menu))


def run():
    if numero_aleatorio == 1:
        while numero_elegido == 2 or 3:
            if numero_elegido == 2:
                print("Ganaste :O, GANADORRRR GAAA, la PC escogió PAPEL")
                break
            else:
                print("¡¡¡Perdiste!!!, PERDEDOR GAAAAAA, la PC escogió PAPEL ")
                break
    elif numero_aleatorio == 2:
        while numero_elegido == 1 or 3:
                if numero_elegido == 1:
                    print("¡¡¡Perdiste!!!, PERDEDOR GAAAAAA, la PC escogió PIEDRA ")
                    break
                else:
                    print("Ganaste :O, GANADORRRR GAAA, la PC escogió PIEDRA")
                    break
    elif numero_aleatorio == 3:
        while numero_elegido == 2 or 1:
            if numero_elegido == 2:   
                print("¡¡¡Perdiste!!!, PERDEDOR GAAAAAA, la PC escogió TIJERAS")
                break
            else:
                print("Ganaste :O, GANADORRRR GAAA, la PC escogió TIJERAS")
                break
    else:
        numero_elegido == numero_aleatorio
        print("¡Es un empate!")
    

if __name__  == "__main__":
    run()


