def insert_voluntary():
    voluntaries = []
    print("Insert the voluntaries")
    print("---------------------------")

    while True:
        item = input(f"Enter the name of the voluntary: (or 'exit') ")
        if item.lower() == "exit":
            break
        voluntaries.append(item)

    show_voluntary(voluntaries)


def show_voluntary(voluntaries):
    for v in voluntaries:
        print(f"Voluntaries Registred: {v}")


if __name__ == "__main__":
    insert_voluntary()
