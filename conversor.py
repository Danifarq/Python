
temperatura = float(input('ingrese la temperatura a convertir:'))
escala = input('es CelCelsius(C) o Fahrenheit(F)?').lower()
if escala=='f':
    resultado=((temperatura - 32 )* 5/9)
elif escala=='c':
    resultado=((temperatura * 9/5) + 32)
else:
    print('La escala es incorrecta')
print(resultado)
