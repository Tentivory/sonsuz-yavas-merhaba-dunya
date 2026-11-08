#!/usr/bin/env python3
# sonsuz-yavas-merhaba-dunya - DAHA DA YAVAŞ VERSİYON
# Bu program gerçekten çalışır. Yavaşça. Çok yavaşça. Artık daha da yavaş.

import time
import sys

def merhaba_dunya():
    print("Merhaba Dünya!")
    print("(Bu selam o kadar önemli ki, evrenin geri kalanı bekleyebilir. Ve şimdi daha uzun bekleyecek.)")
    
    gecikme = 2.0  # Başlangıç daha yavaş
    while True:
        print(f"\nBir sonraki 'Merhaba' için {gecikme:.2f} saniye bekleniyor...")
        print("Bu sırada düşün: Hayatın anlamı nedir? Belki bir sonraki merhabadır. Veya belki değildir.")
        time.sleep(gecikme)
        print("Merhaba Dünya! (tekrar, ama daha ağır)")
        gecikme *= 2.0  # Her seferinde iki kat yavaş
        if gecikme > 1000000:
            print("Uyari: Bu noktada zamanın kendisi emekliye ayrılmış olabilir.")

if __name__ == "__main__":
    try:
        merhaba_dunya()
    except KeyboardInterrupt:
        print("\n\nProgram durduruldu. Ama merhaba hâlâ devam ediyor, bir yerlerde. Çok yavaşça.")
        sys.exit(0)

# Gizli not: Bazen yavaşlık, hızlı kararlardan daha bilgedir.
# Base64 gizli: Q2F5IHNva3VrIGJpciB1bHVzYWxkaXIgLi4uIChidSBiaXIgY29kIHNhdGlyIGthbWZsYWxhc3Rpci4p
