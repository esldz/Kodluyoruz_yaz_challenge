ilk_giris_oran = 1 / 10
ikinci_giris_oran = 1 / 15
bosalma_oran = 1 / 30

toplam_oran = ilk_giris_oran + ikinci_giris_oran - bosalma_oran

dolum_suresi = 1 / toplam_oran

print(f"Havuzun dolması için gereken süre: {dolum_suresi:.2f} saat")

