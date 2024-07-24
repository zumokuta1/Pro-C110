import random

respuesta = "y"

while respuesta == "y":
  numero = random.randint(1, 6)

  print("-----")
  print("|", numero, "|")
  print("-----")

  respuesta = input("¿Quieres tirar el dado de nuevo? (y/n): ")

print("¡Hasta luego!")
