list_laura = set(input("Enter the list of Laura:").lower().split())
list_ana = set(input("Enter the list of Ana:").lower().split())

itens_in_both = list_laura.intersection(list_ana)
exclusive_laura = list_laura.difference(list_ana)
exclusive_ana = list_ana.difference(list_laura)

print(f"Itens in both lists {', '.join(itens_in_both)}")
print(f"Itens exclusive of Laura {', '.join(exclusive_laura)}")
print(f"Itens exclusive of Ana {', '.join(exclusive_ana)}")
