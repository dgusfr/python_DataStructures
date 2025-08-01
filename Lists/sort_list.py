def insert_list():
    score = []
    print("Insert items into the list")
    print("---------------------------")

    for i in range(5):
        item = input(f"Enter the item: {i + 1}: ")
        score.append(item)

    sort_list(score)


def sort_list(score):
    score.sort()
    print("---------------------------")
    print("Sorted list:", score)


if __name__ == "__main__":
    insert_list()
