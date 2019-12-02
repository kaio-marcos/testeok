import re
c = open('BAR2.svg', encoding="UTF-8")
b = open('planta BAR.svg', 'w', encoding="UTF-8")

def remove_2(c, b):
    for i in c:
        print('to aqui')
        print(c)
        z = i
        z = re.sub(r'"<tspan"\s.*\B>', "", i)
        b.write(z)
        print(f"Tag {z}")

remove_2(c, b)

#	for x in f:
#		contar_linha += x.count('<tspan')
#		print(contar_linha) 
#		trocar = re.sub(r"<tspan\s.*\B>", "", x)
#		a.write(trocar)
#		print(f"Tag{x} Removida")
#	f.close()