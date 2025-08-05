participants = {"Mariana": 25, "Carlos": 32, "Beatriz": 28, "Rafael": 35}


def name_of_participants():
    for key in participants.keys():
        print(f"The name of the participants: {key}")


def age_of_participants():
    for value in participants.values():
        print(f"The age of the participants: {value}")


def show_participants():
    print(f"Participants and the ages: ")
    for key, value in participants.items():
        print(f"- {key} : {value} anos")


name_of_participants()
age_of_participants()
show_participants()
