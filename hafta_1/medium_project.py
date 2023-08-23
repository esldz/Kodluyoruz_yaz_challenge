from collections import Counter 

metin = input("Bir metin girin: ") #kullanıcıdan bir metin girmesini istedik.

"""lower ile tüm harfleri küçük yapıp büyük harf
ve küçük harfleri aynı olarak algılamasını sağladık.
replace ile boşlukları karakter olarak saymadı ve 
metindeki karakter sayısını hesapladık"""
karakter_sayilari = Counter(metin.lower().replace(" ", ""))

#en çok tekrar eden karakteri ve kaç tane olduğunu bulduk.
en_cok_tekrar_eden_karakter = karakter_sayilari.most_common(1)[0]

#konsola en çok tekrar eden karakter ve kaç kere tekrar ettiğini yazdırdık.
print("En çok tekrar eden karakter: ",en_cok_tekrar_eden_karakter[0],"\nKaç kere tekrar etti: ",en_cok_tekrar_eden_karakter[1])
