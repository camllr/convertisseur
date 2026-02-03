import tkinter as tk
from converter import (
    convert_distance,
    convert_temperature,
    convert_weight,
    convert_volume,
)

def convert_action():
    try:
        value = float(entry_value.get())
        category = var_category.get()
        from_unit = entry_from.get().strip()
        to_unit = entry_to.get().strip()

        if category == "distance":
            result = convert_distance(value, from_unit.lower(), to_unit.lower())
        elif category == "temperature":
            result = convert_temperature(value, from_unit.upper(), to_unit.upper())
        elif category == "poids":
            result = convert_weight(value, from_unit.lower(), to_unit.lower())
        elif category == "volume":
            result = convert_volume(value, from_unit.lower(), to_unit.lower())
        else:
            raise ValueError("Type de conversion inconnu.")

        label_result.config(text=f"Résultat : {value} {from_unit} = {result} {to_unit}")
    except Exception as e:
        label_result.config(text=f"Erreur : {e}")


root = tk.Tk()
root.title("Convertisseur d'unités")


tk.Label(root, text="Type :").grid(row=0, column=0, sticky="w")
var_category = tk.StringVar(value="distance")
option_category = tk.OptionMenu(
    root,
    var_category,
    "distance",
    "temperature",
    "poids",
    "volume",
)
option_category.grid(row=0, column=1, sticky="w")


tk.Label(root, text="Valeur :").grid(row=1, column=0, sticky="w")
entry_value = tk.Entry(root)
entry_value.grid(row=1, column=1)


tk.Label(root, text="De :").grid(row=2, column=0, sticky="w")
entry_from = tk.Entry(root)
entry_from.grid(row=2, column=1)


tk.Label(root, text="Vers :").grid(row=3, column=0, sticky="w")
entry_to = tk.Entry(root)
entry_to.grid(row=3, column=1)


btn_convert = tk.Button(root, text="Convertir", command=convert_action)
btn_convert.grid(row=4, column=0, columnspan=2, pady=5)


label_result = tk.Label(root, text="Résultat :")
label_result.grid(row=5, column=0, columnspan=2)

root.mainloop()
