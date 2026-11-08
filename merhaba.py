#!/usr/bin/env python3
# sonsuz-yavas-merhaba-dunya
# Bu program gerçekten çalışır. Yavaşça. Çok yavaşça.

import time
import sys

def merhaba_dunya():
    print("Merhaba Dünya!")
    print("(Bu selam o kadar önemli ki, evrenin geri kalanı bekleyebilir.)")
    
    gecikme = 1.0
    while True:
        print(f"\nBir sonraki 'Merhaba' için {gecikme:.2f} saniye bekleniyor...")
        print("Bu sırada düşün: Hayatın anlamı nedir? Belki bir sonraki merhabadır.")
        time.sleep(gecikme)
        print("Merhaba Dünya! (tekrar)")
        gecikme *= 1.5  # Her seferinde %50 daha yavaş
        if gecikme > 1000000:
            print("Uyari: Bu noktada zamanın kendisi sıkılmış olabilir.")

if __name__ == "__main__":
    try:
        merhaba_dunya()
    except KeyboardInterrupt:
        print("\n\nProgram durduruldu. Ama merhaba hâlâ devam ediyor, bir yerlerde.")
        sys.exit(0)

# Gizli not: Bazen yavaşlık, hızlı kararlardan daha bilgedir.
# Base64 gizli: Q2F5IHNva3VrIGJpciB1bHVzYWxkaXIgLi4uIChidSBiaXIgY29kIHNhdGlyIGthbWZsYWxhc3Rpci4p
