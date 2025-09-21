print('hola') #comentario
Libro = 'El programador'
array = [23,24,35]
print (array[0])
jugadores = {
    10: 'Messi',
    7: 'Cristiano Roanldo'
}
print (jugadores[10])

autorizado = True
if autorizado:
    print ('puede pasar')
else:
    print('no puede pasar')
 
entero = 100
if entero==99:
    print('es 99')
elif entero==100:
    print('es 100')
else:
    print('No es 99 ni 100')

color = 'amarillo'
match color:
    case 'verde':
        print('exito')
    case 'amarillo':
        print('advertencia')
    case _:
        print('error')
def sumar(primero, segundo):
    return primero + segundo
resultado = sumar(3,4)
print(resultado)
animales = ['perro', 'gato', 'tigre']
for animal in animales:
    print(animal)
def multiplicar(primero, segundo):
    print(primero*segundo)
numeros = [23,34,45,56,67,78]
for numero in numeros:
    multiplicar (numero, 2)
entero=100
emergencia=911
while entero < emergencia:
    print (entero)
    entero += 1
javascript = {
    'nombre': 'javascript',
    'año' : 1995
}
def descripcion():
    print('%s fue creado en %s' % (javascript['nombre'], javascript['año']))
descripcion() 
class Lenguaje:
    def __init__(self, nombre, año):
        self.nombre= nombre
        self.año = año
def descripcion(self):
    print('%s fue creado en %s' % (self.nombre, self.año))
javascript = Lenguaje('javascript', 1995) 
javascript.descripcion()
html = Lenguaje('HTML', 1993)
html.descripcion()
lenguajes = ["Python","Ruby","PHP","Java Script", "Java"]
for lenguaje in lenguajes:
    print (lenguaje)
    