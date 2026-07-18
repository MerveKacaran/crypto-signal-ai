import asyncio

from app.services.analyzer import analyze_market

# Bellekte tutulacak son analiz sonuçları
latest_signals = []


async def scanner_loop():

    global latest_signals

    while True:

        try:
            print("Market taranıyor...")

            latest_signals = analyze_market()

            print(f"{len(latest_signals)} coin analiz edildi.")

        except Exception as e:
            print("Scanner Hatası:", e)

        await asyncio.sleep(30)
