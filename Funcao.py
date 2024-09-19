a = float(input("Digite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))

print(f"Equação: {a}x² + {b}x + {c} = 0")

delta = b**2 - 4*a*c
x_vertice = -b / (2 * a)
y_vertice = -delta / (4 * a)

if delta > 0:
    # Duas raízes reais
    raiz_delta = delta ** 0.5
    x1 = (-b + raiz_delta) / (2 * a)
    x2 = (-b - raiz_delta) / (2 * a)
    print(f"As raízes da equação são x1 = {x1:.2f} e x2 = {x2:.2f}")

elif delta == 0:
    # Uma raiz real
    x = -b / (2 * a)
    print(f"A raiz da equação é x = {x:.2f}")

else:
    print("A equação não possui raízes reais")

print(f"Vértice da parábola: V(X = {x_vertice:.2f}, Y = {y_vertice:.2f})")