from aircraft import Aircraft
modelo_nave = input("Enter aircraft model:\n")
aircraft = Aircraft(modelo_nave)
while True:
    command = input("Enter command (A for ascent, D for descent, X to exit):\n")
    if command == "X":
        break
    parts = command.split()
    if len(parts) != 2:
        continue
    action, feet = parts
    try:
        feet = int(feet)
    except ValueError:
        continue
    if action == "A":
        aircraft.ascend(feet)
    elif action == "D":
        aircraft.descend(feet)
   
print(f"Final altitude: {aircraft.altitude} feet")