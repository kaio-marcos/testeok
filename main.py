from localiza import ItmDeploy
f = open('BAR.svg', encoding="UTF-8")
#criar arquivo
a = open('planta BAR.svg', 'w', encoding="UTF-8")

d = open('planta BAR.svg', encoding="UTF-8")
b = open('planta BAR2.svg', 'w', encoding="UTF-8")

itm = ItmDeploy

itm.remove_tag(self, f, a)
itm.adiciona_id(self, d, b)