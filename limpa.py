d = open('planta BAR.svg', encoding="UTF-8")

b = open('planta BAR2.svg', 'w', encoding="UTF-8")

for c in d:	
    if '<tspan' in c:
        print(len(c))        
        x = c
        c = x.replace(x,'')        
    print(c)
    b.write(c)            	
d.close