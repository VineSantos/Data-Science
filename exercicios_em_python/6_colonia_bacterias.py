
colonia_A = 4
colonia_B = 10
taxa_crescimento_A = 0.03
taxa_crescimento_B = 0.015

dias = 0

while colonia_A <= colonia_B:
    colonia_A += colonia_A * taxa_crescimento_A
    colonia_B += colonia_B * taxa_crescimento_B
    dias += 1

print(f"Levará {dias} dias para a colônia A ultrapassar ou igualar a colônia B.")
