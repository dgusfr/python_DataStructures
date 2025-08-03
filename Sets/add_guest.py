guests = set()

while True:
    name = input("Enter the name of the guest (or 'exit'): ")
    if name.lower() == "exit":
        break

    guests.add(name)

print("The guests are:")
for guest in guests:
    print(guest)
