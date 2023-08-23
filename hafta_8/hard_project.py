metin = input("Bir metin girin: ")
sesli_harfler = ['a', 'e', 'ı', 'i', 'o', 'ö', 'u', 'ü']

sesli_harf_sayac = 0
sessiz_harf_sayac = 0

for harf in metin:
    if harf.lower() in sesli_harfler:  
        sesli_harf_sayac += 1
    elif harf.isalpha(): 
        sessiz_harf_sayac += 1

print(f"{metin} metinindeki sesli harf sayısı = {sesli_harf_sayac}\nSessiz harf sayısı = {sessiz_harf_sayac}")
