permission = set(["leitura", "escrita", "execução", "compartilhamento"])

solicited_permissions = set(
    input("Enter the permissions you want to request (separated by commas): ").split(
        ", "
    )
)

if solicited_permissions.issubset(permission):
    print("The solicited permissions are valid.")
else:
    print("The permissions are NOT valid.")
