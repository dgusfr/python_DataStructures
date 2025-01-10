my_list = []
my_list.append("novo_elemento")
my_list.remove("elemento_a_remover")
my_list.sort()
my_list.reverse()
length = len(my_list)
if "elemento" in my_list:
    print("O elemento está na lista.")
my_list.insert(2, "elemento_inserido")

copied_list = my_list.copy()
