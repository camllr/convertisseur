# converter.py
distance_units = {
    'm': 1,
    'km': 1000,
    'mi': 1609.34,
    'ft': 0.3048,
    'cm': 0.01,
    'mm': 0.001
}
def convert_distance(value, from_unit, to_unit):
    if from_unit not in distance_units or to_unit not in distance_units:
        raise ValueError("Unité de distance non prise en charge.")
    
    value_in_meters = value * distance_units[from_unit]
    converted_value = value_in_meters / distance_units[to_unit]
    return converted_value


temperature_units = {'C', 'F', 'K'}
def convert_temperature(value, from_unit, to_unit):
    if from_unit not in temperature_units or to_unit not in temperature_units:
        raise ValueError("Unité de température non prise en charge.")
    
    # Convertir d'abord en Celsius
    if from_unit == 'F':
        value_in_celsius = (value - 32) * 5/9
    elif from_unit == 'K':
        value_in_celsius = value - 273.15
    else:
        value_in_celsius = value
    
    # Convertir de Celsius à l'unité cible
    if to_unit == 'F':
        converted_value = (value_in_celsius * 9/5) + 32
    elif to_unit == 'K':
        converted_value = value_in_celsius + 273.15
    else:
        converted_value = value_in_celsius
    
    return converted_value


weight_units = {
    'g': 1,
    'kg': 1000,
    'lb': 453.592,
    'oz': 28.3495
}
def convert_weight(value, from_unit, to_unit):
    if from_unit not in weight_units or to_unit not in weight_units:
        raise ValueError("Unité de poids non prise en charge.")
    
    value_in_grams = value * weight_units[from_unit]
    converted_value = value_in_grams / weight_units[to_unit]
    return converted_value


volume_units = {
    'L': 1,
    'mL': 0.001,
    'gal': 3.78541,
    'qt': 0.946353,
    'cl': 0.01,
    'cup': 0.24
}
def convert_volume(value, from_unit, to_unit):
    if from_unit not in volume_units or to_unit not in volume_units:
        raise ValueError("Unité de volume non prise en charge.")
    
    value_in_liters = value * volume_units[from_unit]
    converted_value = value_in_liters / volume_units[to_unit]
    return converted_value