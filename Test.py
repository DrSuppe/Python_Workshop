#konsolenausgabe
print("Hello World")

#grundlegende Datentypen
ganzeZahl = 1 #int
kommaZahl = 1.3 #float
Wort  = "Wort" # String
Boolean = 3 # False
#TODO Array


# if und elif
if Boolean <= 2:
  print("Falsch")
elif Boolean >=4:
  print("richtig")
else:
  print("didney worl")


#for Schleife
for i in range(0, 101):
  print(i)


#while-Schleife
zaehlervariable = 0
while True:
  zaehlervariable += 1
  print("counter: ", zaehlervariable)
  if zaehlervariable >= 100:
    break
