guests = ["Ana", "Pedro", "Carlos"]


def show_guests(guests):
    print(f"Actual list of guests: {guests}")


show_guests(guests)

guest = input("Enter the name of the new guest:")
index = int(input("Enter the index where you want to add the guest:"))

if 0 <= index < len(guests):
    guests.insert(index, guest)
else:
    print("Index out of range")

show_guests(guests)
