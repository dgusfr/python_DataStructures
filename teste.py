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
my_list.clear()
index = my_list.index("elemento_procurado")
count = my_list.count("elemento_repetido")
new_list = my_list + ["novo_elemento_1", "novo_elemento_2"]
for item in my_list:
    print(item)
last_element = my_list.pop()
sub_list = my_list[1:4]
filtered_list = [x for x in my_list if "criterio" in x]
string_to_list = "a,b,c".split(",")
list_to_string = ",".join(my_list)
repeated_list = my_list * 3
