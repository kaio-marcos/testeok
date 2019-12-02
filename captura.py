f = open('BAR.svg', encoding="UTF-8")
a = open('BAR2.svg', 'w', encoding="UTF-8")

def  remove(f, a):
	for x in f:
		c = f
		c = x.replace('</tspan>', '')
		a.write(c)
		print(x)
	f.close

remove(f, a)
