from fractions import Fraction

toplam_kirmizi = 5
toplam_yesil = 4
toplam_mavi = 3
toplam_toplar = toplam_kirmizi + toplam_yesil + toplam_mavi

ayni_renk_olasiligi = Fraction(toplam_kirmizi, toplam_toplar) * Fraction(toplam_kirmizi - 1, toplam_toplar - 1) + Fraction(toplam_yesil, toplam_toplar) * Fraction(toplam_yesil - 1, toplam_toplar - 1) + Fraction(toplam_mavi, toplam_toplar) * Fraction(toplam_mavi - 1, toplam_toplar - 1)

print(f"Aynı renkli iki top olma olasılığı:{ayni_renk_olasiligi}")
