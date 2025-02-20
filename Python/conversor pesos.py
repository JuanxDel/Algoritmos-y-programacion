#Entradas
a = float(input("Chelines Austriacos a pesetas: "))
b = float(input("Dracmas griegos a Francos Franceses: "))
c = float(input("Pesetas a dolares y liras italianas"))
#Caja Negra
c1 = (a*9.56)
c2 = (b*0.044)
c3_1 = (c*0.0081)
c3_2 = (c/0.0009289)
#Salida
print ("Chelines Austriacos a pesetas: ", c1)
print ("Dracmas griegos a Francos Franceses: ", c2)
print ("Pesetas a dolares", c3_1,"y liras italianas", c3_2)