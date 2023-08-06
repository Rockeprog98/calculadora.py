# Calculadora de peso corporal

#Sección de bienvenida para el usuario
print ('Calculadora de índice de la masa corporal')
print('Introduzca el número de usuarios que evaluarán su IMC' )

personas = int(input('Número de usuarios: ')) #Aquí pedimos que se introduzca el número de usuarios, puede ser utilizado por una familia.

while personas > 0:

 nombre = input('Introducir nombre(s): ') #El usuario introduce su o sus nombres.
 a_paterno = input('Introducir apellido paterno: ')
 a_materno = input('Introducir apellido materno: ')
 print ('Bienvenido (a) ' + nombre,  a_paterno,  a_materno)
 edad = int(input ('¿Qué edad tienes?  '))

 # He dividido la calculadora en una sección para niños y otra para adultos dependiendo de la edad introducida.

 if(edad < 18):
   print(nombre,', eres menor de edad')
   altura = float(input('Introduce tu estatura en metros  '))
   peso = float(input('Introduce tu peso en kilos  '))
   IMC = peso / altura ** 2
   print (nombre,', tu índice de masa corporal es ' + str(IMC))

   # La sección para menores de edad se comunica con el usuario "tuteando" a la persona y he incluido algunas pequeñas expresiones.

   if IMC >= 0 and IMC <= 18.9:
    print ('Tu IMC indica que eres una persona con bajo peso :( , por favor consulta a tu nutriólogo. ')
   elif IMC >= 18.5 and IMC <= 24.99:
    print ('Tu IMC indica que eres una persona con peso normal :) , continúa con tus hábitos físicos y alimenticios.')
   elif IMC >= 25.0 and IMC <= 29.99: 
    print ('Tu IMC indica que eres una persona con sobrepeso :( , por favor consulta a tu nutriólogo.')
   elif IMC >= 30.0 and IMC <= 34.99: 
    print ('Tu IMC indica que eres una persona con obesidad leve :( , por favor consulta a tu nutriólogo.')
   elif IMC >= 35.0 and IMC <= 39.99:
    print ('Tu IMC indica que eres una persona con obesidad media :( , por favor consulta a tu nutriólogo.')
   elif IMC > 40:
    print ('Tu IMC indica que eres una persona con obesidad mórbida :v , por favor consulta a tu médico y a tu nutriólogo.')

   print('¡Gracias, cuida de tu salud!')

   #La sección para los mayores de edad se comunica con el usuario de manera formal

 else:
  print(nombre,', usted es mayor de edad')
  altura = float(input('Introduzca su estatura en metros  '))
  peso = float(input('Introduzca su peso en kilos  '))
  IMC = peso / altura ** 2
  print (nombre, ', su índice de masa corporal es ' + str(IMC))
 

  if IMC >= 0 and IMC <= 18.9:
   print ('Su IMC indica que usted es una persona con peso bajo, por favor consulte a su nutriólogo.')
  elif IMC >= 18.5 and IMC <= 24.99:
   print ('Su IMC indica que usted es una persona con peso normal, continúe con sus hábitos físicos y alimenticios.')
  elif IMC >= 25.0 and IMC <= 29.99: 
   print ('Su IMC indica que usted es una persona con sobrepeso, por favor consulte a su nutriólogo.')
  elif IMC >= 30.0 and IMC <= 34.99: 
   print ('Su IMC indica que usted es una persona con obesidad leve, por favor consulte a su nutriólogo.')
  elif IMC >= 35.0 and IMC <= 39.99:
   print ('Su IMC indica que usted es una persona con obesidad media, por favor consulte a su nutriólogo.')
  elif IMC > 40:
   print ('Su IMC indica que usted es una persona con obesidad mórbida, por favor consulte a su médico y a su nutriólogo.')

  print('¡Gracias, cuide de su salud!')
 
 personas = personas - 1 

 
