equipe_a = {"planejar reunião", "revisar documento", "testar sistema"}

equipe_b = {"testar sistema", "implementar funcionalidade", "corrigir bug"}

services = equipe_a.symmetric_difference(equipe_b)

print("Serviços exclusivos de cada equipe:", services)
