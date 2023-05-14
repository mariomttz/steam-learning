datos = list(map(int,input().split()))

resultado = (datos[0] * 100)/(datos[0] + datos[1])

if 0 <= resultado <= 20:
    resultado = 1
elif 20 < resultado <= 40:
    resultado = 2
elif 40 < resultado <= 60:
    resultado = 3
elif 60 < resultado <= 80:
    resultado = 4
elif 80 < resultado <= 100:
    resultado = 5

print(resultado)