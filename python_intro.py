print('Hello, Django girls!')

if 3 > 2:
   print('It works!')
if 5 > 2: 
	print('5 is indeed greater than 2')
else:
	print('5 is not greater than 2')
name = 'Sonia'
if name == 'Hola':
	print('Hey Hola!')
elif name == 'Sonia':
	print('Hey Sonia!')
else:
    print('Hey anonimo!')


volume = 57
if volume < 20:
    print("It's kinda quiet.")
elif 20 <= volume < 40:
    print("It's nice for background music")
elif 40 <= volume < 60:
    print("Perfect, I can hear all the details")
elif 60 <= volume < 80:
    print("Nice for parties")
elif 80 <= volume < 100:
    print("A bit loud!")
else:
    print("Me duelen las orejas! :(")


# la palabra definida al final con parentesis es
#para activar la funcion, si no se pone, no la imprime

def Hola():
	print ('Oye tu!')
	print ('Como estas?')
Hola() 


#agregando la funcion de nombre

def ola(nombre):
	if nombre == 'Hola':
		print('Hey Hola!')
	elif nombre == 'Sonia':
		print('Hey Sonia!')
	else:
		print('Hey anonimo!')
ola('nombre')

#varias funciones al mismo tiempo

def hola(name):
	print ('hola ' +name+'!')

hola("Raquel")


#hacer una lista de personas
#en codigos

def hola(nombres):
	print('Hola ' +nombres+ '!')
chicas = ['Raquel', 'Monica', 'Sofia', 'Maria', 'Karo']
for nombres in chicas:	
	hola(nombres)
	print('Siguiente chica')


	#limite inferior y superior range

for i in range(1, 6):
	print(i)