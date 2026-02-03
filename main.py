# main.py
# 1. afficher un menu
# 2. demander à l'utilisateur ce qu'il veut convertir
# 3. appeler les bonnes fonctions de converter.py
# 4. afficher le résultat

from converter import (
  convert_distance,
  convert_temperature,
  convert_weight,
  convert_volume,
  ask_restart
)

from datetime import datetime

def log_history(category, value, from_unit, to_unit, result):
    with open("history.txt", "a", encoding="utf-8") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        line = f"[{timestamp}] {category}: {value} {from_unit} -> {result} {to_unit}\n"
        f.write(line)

def main(): 
    print("Bienvenue dans le convertisseur d'unités! Souhaitez-vous convertir aujourd'hui?")

    demarrage = input("Entrez 'oui' pour continuer ou 'non' pour quitter: ").strip().lower()
    if demarrage == 'non':
        print("Au revoir!")
        return

    while True:
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
          if not ask_restart():
              print("Au revoir!")
              return 
      elif choice == '2':
          convert_temperature_interface()
          if not ask_restart():
              print("Au revoir!")
              return
      elif choice == '3':
          convert_weight_interface()
          if not ask_restart():
              print("Au revoir!")
              return
      elif choice == '4':
          convert_volume_interface()
          if not ask_restart():
              print("Au revoir!")
              return
      else:
          print("Choix invalide. Veuillez réessayer.")



def convert_distance_interface():
    while True:
      try:
        value = float(input("Entrez la valeur à convertir: "))
        break
      except ValueError:
        print("Veuillez entrer une valeur numérique valide.")
      
    valid_units = ['m', 'km', 'mi', 'ft', 'cm', 'mm']
    while True:
      from_unit = input("Entrez l'unité de départ (m, km, mi, ft, cm, mm): ").strip().lower()
      if from_unit in valid_units:
        break
      else:
        print("Unité invalide. Veuillez réessayer.")

    while True:
      to_unit = input("Entrez l'unité cible (m, km, mi, ft, cm, mm): ").strip().lower() 
      if to_unit in valid_units:
        break
      else:
        print("Unité invalide. Veuillez réessayer.")

    try:
        result = convert_distance(value, from_unit, to_unit)
        print(f"{value} {from_unit} = {round(result, 4)} {to_unit}")
        log_history("Distance", value, from_unit, to_unit, result)
    except ValueError as e:
        print(e)


def convert_temperature_interface():
    while True:
      try:
        value = float(input("Entrez la valeur à convertir: "))
        break
      except ValueError:
        print("Veuillez entrer une valeur numérique valide.")

    valid_units = ['C', 'F', 'K']
    while True:
      from_unit = input("Entrez l'unité de départ (C, F, K): ").strip().upper()
      if from_unit in valid_units:
        break
      else:
        print("Unité invalide. Veuillez réessayer.")
    
    while True:
      to_unit = input("Entrez l'unité cible (C, F, K): ").strip().upper()
      if to_unit in valid_units:
        break
      else:
        print("Unité invalide. Veuillez réessayer.")
        
    try:
        result = convert_temperature(value, from_unit, to_unit)
        print(f"{value} {from_unit} = {round(result, 4)} {to_unit}")
        log_history("Temperature", value, from_unit, to_unit, result)
    except ValueError as e:
        print(e)


def convert_weight_interface():
    while True:
      try:
        value = float(input("Entrez la valeur à convertir: "))
        break
      except ValueError:
        print("Veuillez entrer une valeur numérique valide.")

    valid_units = ['g', 'kg', 'lb', 'oz']
    while True:
      from_unit = input("Entrez l'unité de départ (g, kg, lb, oz): ").strip().lower()
      if from_unit in valid_units:
        break
      else:
        print("Unité invalide. Veuillez réessayer.")

    while True:
      to_unit = input("Entrez l'unité cible (g, kg, lb, oz): ").strip().lower()
      if to_unit in valid_units:
        break
      else:
        print("Unité invalide. Veuillez réessayer.")

    try:
        result = convert_weight(value, from_unit, to_unit)
        print(f"{value} {from_unit} = {round(result, 4)} {to_unit}")
        log_history("Weight", value, from_unit, to_unit, result)
    except ValueError as e:
        print(e)


def convert_volume_interface():
    while True:
      try:
        value = float(input("Entrez la valeur à convertir: "))
        break
      except ValueError:
        print("Veuillez entrer une valeur numérique valide.")

    valid_units = ['l', 'ml', 'gal', 'qt', 'cl', 'cup']
    while True:
      from_unit = input("Entrez l'unité de départ (L, mL, gal, qt, cl, cup): ").strip().lower()
      if from_unit in valid_units:
        break
      else:
        print("Unité invalide. Veuillez réessayer.")
    
    while True:
      to_unit = input("Entrez l'unité cible (L, mL, gal, qt, cl, cup): ").strip().lower()
      if to_unit in valid_units:
        break
      else:
        print("Unité invalide. Veuillez réessayer.")

    try:
        result = convert_volume(value, from_unit, to_unit)
        print(f"{value} {from_unit} = {round(result, 4)} {to_unit}")
        log_history("Volume", value, from_unit, to_unit, result)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
