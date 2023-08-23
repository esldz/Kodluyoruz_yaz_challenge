from datetime import datetime #datetime kütüphanesini projemize yüklendi

now_year = datetime.now().year #şuanki yılı now_year değişkenine yazıldı

dg_year=int(input("Doğum yılınız: ")) #kullanıcıdan yaşını integer değerinde girmesini istedik.

age=now_year-dg_year #şuanki yıldan doğum yılını çıkartarak yaşı buldundu
print("Yaşınız: ",age) #konsola yaşı yazdırıldı