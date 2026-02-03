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

        label_result.config(
            text=f"Résultat : {value} {from_unit} = {result} {to_unit}",
            fg="#222222",
        )
    except Exception as e:
        label_result.config(text=f"Erreur : {e}", fg="#b00020")


# --- Fenêtre principale et style ---

root = tk.Tk()
root.title("Convertisseur d'unités")
root.geometry("400x260")
root.resizable(False, False)

BG_COLOR = "#f5f5f5"
BTN_COLOR = "#4CAF50"
BTN_COLOR_ACTIVE = "#45a049"
BTN_FG = "#ffffff"
TEXT_COLOR = "#333333"
DEFAULT_FONT = ("Arial", 11)

root.configure(bg=BG_COLOR)

# Colonnes à largeur égale (pour centrer)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

# --- Ligne 0 : type de conversion (centré via un Frame) ---

top_frame = tk.Frame(root, bg=BG_COLOR)
top_frame.grid(row=0, column=0, columnspan=2, pady=10)

label_type = tk.Label(
    top_frame,
    text="Type :",
    font=DEFAULT_FONT,
    bg=BG_COLOR,
    fg=TEXT_COLOR,
)
label_type.pack(side="left", padx=5)

var_category = tk.StringVar(value="distance")
option_category = tk.OptionMenu(
    top_frame,
    var_category,
    "distance",
    "temperature",
    "poids",
    "volume",
)
option_category.config(font=DEFAULT_FONT)
option_category.pack(side="left", padx=5)

# --- Ligne 1 : valeur ---

label_value = tk.Label(
    root,
    text="Valeur :",
    font=DEFAULT_FONT,
    bg=BG_COLOR,
    fg=TEXT_COLOR,
)
label_value.grid(row=1, column=0, sticky="e", padx=10, pady=5)

entry_value = tk.Entry(root, font=DEFAULT_FONT)
entry_value.grid(row=1, column=1, padx=10, pady=5)

# --- Ligne 2 : unité de départ ---

label_from = tk.Label(
    root,
    text="De :",
    font=DEFAULT_FONT,
    bg=BG_COLOR,
    fg=TEXT_COLOR,
)
label_from.grid(row=2, column=0, sticky="e", padx=10, pady=5)

entry_from = tk.Entry(root, font=DEFAULT_FONT)
entry_from.grid(row=2, column=1, padx=10, pady=5)

# --- Ligne 3 : unité cible ---

label_to = tk.Label(
    root,
    text="Vers :",
    font=DEFAULT_FONT,
    bg=BG_COLOR,
    fg=TEXT_COLOR,
)
label_to.grid(row=3, column=0, sticky="e", padx=10, pady=5)

entry_to = tk.Entry(root, font=DEFAULT_FONT)
entry_to.grid(row=3, column=1, padx=10, pady=5)

# --- Ligne 4 : bouton Convertir (centré sur 2 colonnes) ---

btn_convert = tk.Button(
    root,
    text="Convertir",
    command=convert_action,
    font=DEFAULT_FONT,
    bg=BTN_COLOR,
    fg=BTN_FG,
    activebackground=BTN_COLOR_ACTIVE,
    activeforeground=BTN_FG,
)
btn_convert.grid(row=4, column=0, columnspan=2, pady=10)

# --- Ligne 5 : résultat (centré sur 2 colonnes) ---

label_result = tk.Label(
    root,
    text="Résultat :",
    font=DEFAULT_FONT,
    bg=BG_COLOR,
    fg=TEXT_COLOR,
)
label_result.grid(row=5, column=0, columnspan=2, pady=5)

root.mainloop()
