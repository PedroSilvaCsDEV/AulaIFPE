d = 20  # diâmetro (mm)
l = 800  # comprimento (mm)
F = 7200  # carga (N)
E = 210000  # módulo de elasticidade do aço (MPa)
V = 0.3  # coeficiente de Poisson

# a) Tensão normal (sigma)
A = 3.14 * (d / 2) ** 2  # área (mm²)
o = F / A  # tensão normal (MPa)

# b) Deformação longitudinal (epsilon) pela Lei de Hooke
e = o / E  # deformação longitudinal
e_micro = e * 1e6  # convertendo para micrometros (μ)

# c) Alongamento (delta l)
Dl = e * l  # alongamento (mm)
Dl_micro = Dl * 1e3  # convertendo para micrometros (μm)

# d) Deformação transversal (epsilon_t)
et = -V * e  # deformação transversal
et_micro = et * 1e6  # convertendo para micrometros (u)

print(f"Tensão normal (sigma): {o:.1f} MPa")
print(f"Alongamento (delta l): {Dl_micro:.1f} um")
print(f"Deformação longitudinal (epsilon): {e_micro:.1f} u")
print(f"Deformação transversal (epsilon_t): {et_micro:.1f} u")