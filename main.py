import game

type = int(input("\nEscolha o tipo: \n\n[1] - Python\n[2] - Java\n\n>>> ")) - 1

types = [ "python", "java" ]

print(f"\nJogo iniciando! Modo: {types[type].capitalize()}\n")

game.run(types[type])