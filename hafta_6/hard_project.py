cumle = input("içindeki ikilem bulunan cümle giriniz: ")
kelimeler = cumle.split()
ikilem_var = False

for i in range(len(kelimeler) - 1):
    if kelimeler[i] == kelimeler[i + 1]:
        ikilem_var = True
        break

if ikilem_var:
    print("Bu cümlede ikilem vardır.")
else:
    print("Bu cümlede ikilem yoktur.")
