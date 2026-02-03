# main.py
# 1. afficher un menu
# 2. demander à l'utilisateur ce qu'il veut convertir
# 3. appeler les bonnes fonctions de converter.py
# 4. afficher le résultat


from converter import (
  convert_distance,
  convert_temperature,
  convert_weight,
  convert_volume
)

def main():
    while True: 
      print("Bienvenue dans le convertisseur d'unités!")
      print("Choisissez le type de conversion:")
      print("1. Distance")
      print("2. Température")
      print("3. Poids")
      print("4. Volume")
      print("0. Quitter")
      
      choice = input("Entrez le numéro de votre choix: ")
      
      if choice == '0':
          print("Au revoir!")
          return
      elif choice == '1':
          convert_distance_interface() 
      elif choice == '2':
          convert_temperature_interface()
      elif choice == '3':
          convert_weight_interface()
      elif choice == '4':
          convert_volume_interface()
      else:
          print("Choix invalide. Veuillez réessayer.")

def convert_distance_interface():
    value = float(input("Entrez la valeur à convertir: "))
    from_unit = input("Entrez l'unité de départ (m, km, mi, ft, cm, mm): ")
    to_unit = input("Entrez l'unité cible (m, km, mi, ft, cm, mm): ")
    try:
        result = convert_distance(value, from_unit, to_unit)
        print(f"{value} {from_unit} = {result} {to_unit}")
    except ValueError as e:
        print(e)

def convert_temperature_interface():
    value = float(input("Entrez la valeur à convertir: "))
    from_unit = input("Entrez l'unité de départ (C, F, K): ")
    to_unit = input("Entrez l'unité cible (C, F, K): ")
    try:
        result = convert_temperature(value, from_unit, to_unit)
        print(f"{value} {from_unit} = {result} {to_unit}")
    except ValueError as e:
        print(e)

def convert_weight_interface():
    value = float(input("Entrez la valeur à convertir: "))
    from_unit = input("Entrez l'unité de départ (g, kg, lb, oz): ")
    to_unit = input("Entrez l'unité cible (g, kg, lb, oz): ")
    try:
        result = convert_weight(value, from_unit, to_unit)
        print(f"{value} {from_unit} = {result} {to_unit}")
    except ValueError as e:
        print(e)

def convert_volume_interface():
    value = float(input("Entrez la valeur à convertir: "))
    from_unit = input("Entrez l'unité de départ (L, mL, gal): ")
    to_unit = input("Entrez l'unité cible (L, mL, gal): ")
    try:
        result = convert_volume(value, from_unit, to_unit)
        print(f"{value} {from_unit} = {result} {to_unit}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
