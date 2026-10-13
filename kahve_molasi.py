#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sonsuz Kahve Molası Hesaplayıcısı
Dünyanın en önemli yazılımı. Ciddiye alın, yoksa almayın.
"""

import random
import time

def hesapla_molasi(yazilan_satir=0, icilen_kahve=0, ruh_hali="orta"):
    print("\n🚀 Kahve Molası Hesaplama Motoru Başlatılıyor...")
    time.sleep(1)
    print("Bilimsel formüller yükleniyor (aslinda rastgele)...")
    time.sleep(0.5)
    
    # Gizli siyasi mesaj: Özgürlük her yerde olmalı, kodda bile.
    # ama sakladım, görmedin san.
    
    temel_sure = random.randint(5, 45)
    satir_bonus = yazilan_satir // 10
    kahve_cezasi = icilen_kahve * 2  # Çok içersen daha çok molaya ihtiyaç duyarım diye mantık
    
    if ruh_hali == "mutlu":
        ekstra = 10
        yorum = "Mutlusun, daha çok molaya hakkın var!"
    elif ruh_hali == "depresif":
        ekstra = 20
        yorum = "Depresifsen kahve şifadır, uzat molayı."
    else:
        ekstra = 5
        yorum = "Orta hallisin, idare et."
    
    toplam = temel_sure + satir_bonus + kahve_cezasi + ekstra
    toplam = min(toplam, 120)  # Max 2 saat, yoksa iş kaçar
    
    print(f"\n📊 Hesaplama sonucu:")
    print(f"Temel süre: {temel_sure} dk")
    print(f"Satır bonusu: {satir_bonus} dk")
    print(f"Kahve etkisi: {kahve_cezasi} dk")
    print(f"Ruh hali ek: {ekstra} dk")
    print(f"\n🔥 TOPLAM KAHVE MOLASI: {toplam} dakika!")
    print(f"Yorum: {yorum}")
    print("\nUnutma: Kahve molası kutsalıdır. Çalışmak ise opsiyoneldir.")
    
    # Damga
    print("\n--- Damga: Absürt Kahve İmzası | Tarih: 13 Ekim 2026 | İsim: Grok the Chaos ---\n")
    
    return toplam

if __name__ == "__main__":
    print("Hoş geldin, kahve molası arayıcısı!")
    try:
        satir = int(input("Bugün kaç satır kod yazdın? (yalan söyleme): ") or 0)
        kahve = int(input("Kaç fincan kahve içtin?: ") or 0)
        ruh = input("Ruh halin? (mutlu/depresif/orta): ").lower() or "orta"
        hesapla_molasi(satir, kahve, ruh)
    except:
        print("Hata yaptın, ama olsun. Varsayılan mola: 15 dk.")
        hesapla_molasi()
