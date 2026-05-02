from aircraft import Aircraft

model = input("Enter aircraft model:\n")
aircraft = Aircraft(model)

while True:
    command = input("Enter command (A for ascent, D for descent, X to exit):\n").strip()
    if command.upper() == "X":
        break
    parts = command.split()
    if len(parts) != 2:
        continue
    action = parts[0].upper()
    value = parts[1]
    try:
        feet = int(value)
    except ValueError:
        continue
    if action == "A":
        aircraft.ascend(feet)
    elif action == "D":
        aircraft.descend(feet)
print(f"Final altitude: {aircraft.altitude} feet")