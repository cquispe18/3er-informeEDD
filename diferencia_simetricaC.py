conjunto1=[1,2,3,4,5,6,7,8,9,10,11]
conjunto2=[2,4,6,8,10]
conjunto3=[1,3,5,7,11]

A=set(conjunto1)
B=set(conjunto2)
C=set(conjunto3)

diferenciaSimetrica=A^B^C
print("LA DIFERENCIA SIMETRICA ENTRE LOS CONJUNTOS A,B Y C ES: ",diferenciaSimetrica)