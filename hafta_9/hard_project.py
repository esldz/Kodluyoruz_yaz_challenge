sayi = int(input("Sayı girin: "))

rakamlar = [1, 2, 3, 4, 5, 6, 7, 8, 9]
kok_bulundu = False

for rakam in rakamlar:
    if rakam * rakam == sayi:
        print(f"{sayi} sayısı kökten {rakam} olarak çıkar.")
        kok_bulundu = True
        break

if not kok_bulundu:
    print(f"{sayi} sayısı kökten çıkmaz.")
