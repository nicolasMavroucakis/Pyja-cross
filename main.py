import game
import connection
connection.connect()

type = int(input("\nEscolha o tipo: \n\n[1] - Python\n[2] - Java\n\n>>> ")) - 1

types = [ "python", "java" ]

userRa = input("\nSeu RA: ")
userId = connection.getUserId(userRa)

print(f"\n\nJogo iniciando! Modo: {types[type].capitalize()}\nRA: {userRa}\nID: {userId}")

game.run(types[type], userId, type)