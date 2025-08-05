participants = {
    "Workshop 1": {"Alice", "Bruno", "Carla", "Diego"},
    "Workshop 2": {"Fernanda", "Gustavo", "Helena"},
}


def remove_participants(participant):
    if participant in participants["Workshop 1"]:
        participants["Workshop 1"].discard(participant)
        print(f"{participant} has been removed from Workshop 1.")
    elif participant in participants["Workshop 2"]:
        participants["Workshop 2"].discard(participant)
        print(f"{participant} has been removed from Workshop 2.")
    else:
        print("The participant is not in any Workshop ")


name = input("Enter the name of the participant to remove:")
remove_participants(name)
