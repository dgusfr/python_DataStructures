list = ["Ana", "João", "Pedro"]


def replace_name():
    wrong_name = input("Enter the name to replace: ")

    if wrong_name in list:
        right_name = input("Enter the right name:")
        index = list.index(wrong_name)
        list.remove(wrong_name)
        list.insert(index, right_name)
        print(list)
    else:
        print(f"{wrong_name} not found in the list.")


if __name__ == "__main__":
    replace_name()
