import re

roman_num = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000, "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
Roman = 'III'
Numlist = [roman_num[list(Roman)[i]] for i in range(len(Roman))]
i=0
somme=0
print(Numlist)
while i < len(Numlist):
    print(i,somme)
    if i != len(Numlist)-1 and (Numlist[i]%Numlist[i+1] == 1 or Numlist[i]%Numlist[i+1] == 10 or Numlist[i]%Numlist[i+1] == 100):
        somme += Numlist[i+1] - Numlist[i]
        i += 2
    else:
        somme += Numlist[i]
        i +=1
print(somme)

'''sous = re.findall('IV',Roman) + re.findall('IX',Roman) + re.findall('XL',Roman) + re.findall('XC',Roman) + re.findall('CD',Roman) + re.findall('CM',Roman)
add = Roman
print(sous)
for i in range(len(sous)):
    print(add)
    add = re.sub(sous[i],"",add)
print("\n",add,sous)
sous = [roman_num[sous[i]] for i in range(len(sous))]
add = [roman_num[list(add)[i]] for i in range(len(add))]
print(sum(add)+sum(sous))
'''