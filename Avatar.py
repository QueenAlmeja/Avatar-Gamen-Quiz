import random #usamos la funcion import random para que las preguntas salgan de manera aleatoria 

#Creamos un diccionario donde almacenamos las preguntas y las preguntas
questions_anwser = {"¿Cuales son los maestros originales de cada elemento?": 
            {"a":["Los tejones topos", "La luna", "Los bisontes voladores ", "Los dragones"],
             "b":["Las avispas halcon","Los leones tortugas", "Los cabellos elefantes", "Los pinguinos nutria"],
             "c":["El cometa sozin", "El ladron de rostros", "La dama de agua", "Momo"]},
            "¿Quién es la novia del principe Suko?": {"a":"Katara", "b":"Suki", "c":"Toph","d":"Mai"},
            "¿Cual es el nombre del ladron de Rostros ":{"a":"Koh", "b":"Raava", "c":"Tui", "d":"Wan Shi Tong"},
            "¿Quién es la primera persona en enseñarle fuego control a Aang?":{"a":"Roku", "b":"Azula", "c":"Jeong Jeong", "d":"Suko"},}
#Te encuenta que en este diccionario, las preguntas son las keys y las respuestas estan en los values


#Definimos nuestra primera funcion 
def saludo():
    print("Si eres un gran fan de la Serie:\nAvatar el ultimo maestro aire, este juego sera super fácil para ti")

    print("Este 🎮 es de opciones multilples y por cada opción incorrecta perderas 🩷")
    print("Tienens 5 vidas, así que suerte joven maestro ")

saludo()

def nation():

    player_names = input("Cual es tu nombre joven maestro?: ").capitalize()
    nation_player = input("A que nacion perteneces?: ").capitalize()
    nation_player_list = ["Aire", "Fuego", "Tierra", "Agua"]

    if nation_player not in nation_player_list:
        print(f"{player_names}, no eres parte de ninguna nacion 😔 ")
        exit()
    elif nation_player in nation_player_list:
        print(f"{player_names}, genial eres parte de la nacion {nation_player}")
        print("Veamos que tal te va en este juego")
    
nation() #ejecutamos la funcion que saluda al user 


points = 0 #variable donde ira acumulando puntos 
life = 5 #cantidad de vidas que tienen el jugador 
random.shuffle(questions_anwser.keys()) #esto me permitira que las preguntas se intercalen en cada ronda 
  
for i in range(len(questions_anwser)):
    question = list(questions_anwser.keys())[i]
    answers = questions_anwser[question]
    correct_answer = random.choice(list(answers.values()))
    
    print(f"\n{question}")
    for key, value in answers.items():
        print(f"{key}: {value}")