
import dos

# Programa principal
print ("Inicio del programa principal")

lista = ["Javier"]


entrada1 = input ("nombre: ")

dos.he_dicho(entrada1)

cuantos = lista.count(entrada1)

if cuantos > 0:
	texto = "Ya hay un {} en la lista"
	print (texto.format(entrada1))
else:
	lista.append(entrada1)

for x in lista:
	print (x)


