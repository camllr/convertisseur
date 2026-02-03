from datetime import datetime

def log_history(category, value, from_unit, to_unit, result):
    with open("history.txt", "a", encoding="utf-8") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        line = f"[{timestamp}] {category}: {value} {from_unit} -> {result} {to_unit}\n"
        f.write(line)