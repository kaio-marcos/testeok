import os
import re
def  remove_tag():
	# -*- coding: utf-8 -*-
	f = open(r'BAR.svg', encoding="UTF-8")
	#criar arquivo
	a = open(r'planta BAR.svg', 'w', encoding="UTF-8")
	#abrir o arquivo já existente
#	d = open(r'planta BAR.svg', encoding="UTF-8")
#	b = open(r'planta BAR2.svg', 'w', encoding="UTF-8")
#	contar_linha = 0
	for y in f:
		if '</tspan>' in f:
			f = y.replace('</tspan>', '')
			a.write(f)
	f.close
#	for x in f:
#		contar_linha += x.count('<tspan')
#		print(contar_linha) 
#		trocar = re.sub(r"<tspan\s.*\B>", "", x)
#		a.write(trocar)
#		print(f"Tag{x} Removida")
#	f.close()

''
'exclui pasta'
''
def remove_arquivos():
	cont = 0
	while(cont <= 1):
		caminho = input("Digite o nome da pasta: ")
		arquivo = input("Digite o nome do arquivo: ")
		pasta = f"C:\\Users\\ksilva\\Desktop\\{caminho}"
		dire = os.listdir(pasta)
		for file in dire:
			if file == arquivo:
				os.remove(arquivo)
				print(f'Arquivo {arquivo} removido com sucesso') 
		print(dir)
		cont = cont + 1
#remove_arquivos()

remove_tag()




#d = open('planta BAR.svg', encoding="UTF-8")
#b = open('planta BAR2.svg', 'w', encoding="UTF-8")

#def adiciona_id(d, b):
#	for c in d:	
#		if '<tspan' in c:
#			print(len(c))        
#			x = c
#			c = x.replace(x,'')        
#			print(c)
#			b.write(c)            	
#	d.close

#	for i in d:
#		trocar_dois = re.sub(r"</tspan>", "", i)
#		b.write(trocar_dois)
#		print(f"Tag {i} Removida")
#	f.close()