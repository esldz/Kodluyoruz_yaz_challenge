Cost= 100
Price= 150

sayac=1

while Price-Cost<150:
    sayac+=1
    Cost+=Cost
    Price+=Price

print(f"kar edilmesi için {sayac} tane ürün satılması gerekiyor.")
