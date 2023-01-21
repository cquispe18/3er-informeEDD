#union de conjuntos
ventas1={"zanahorias","papas","mangos","platanos","peras"}
ventas2={"papas","ciruelos","granadillas","mangos","fresa"}
print(ventas1)
ventas3=set()
ventas2.add("pacay")
print(ventas2)
ventas2.remove("ciruelos")
print(ventas2)
print(ventas1|ventas2)