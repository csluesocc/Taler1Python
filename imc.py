print"""
********************************
*                              *
*       Calcula Tu IMC         *
*                              *
*                              *
********************************"""
print ""




print "Para calcular tu IMC has lo siguiente :):"

print""

print "Ingresa tu peso:"
peso=input()

print "ingresa tu Estatura:"
estatura=input()

calc= pow(estatura, 2)
resultado= calc / peso
round(resultado, 1)


print"tu masa corporal es de:",resultado

print" calculado Imc adecuado a tu edad:"

print"Ingresa tu Edad:"
edad=input()
if edad>=19 and edad <=24:

   print"tu IMC es ideal a tu edad"
else:
   print"Tienes un Imc fuera de lo normal"




