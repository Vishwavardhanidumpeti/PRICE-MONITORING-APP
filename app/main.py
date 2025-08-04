from amazon import search_amazon
from utils import send_email
import pandas as pd
import time
from datetime import datetime

def run_monitor(product, budget, run_duration_seconds):
    start_time = time.time()
    all_results = []

    print(f"⏱️ Monitoring Amazon for {run_duration_seconds} seconds...")

    while (time.time() - start_time) < run_duration_seconds:
        print(f"\n🔄 Checking at {datetime.now().strftime('%H:%M:%S')}")

        amazon_results = search_amazon(product)
        print(f"✅ Amazon results: {len(amazon_results)}")

        all_results.extend(amazon_results)

        time.sleep(5)

    print("\n⏱️  Filtering best deals...")

    filtered = [item for item in all_results if item['price'] <= budget]

    if filtered:
        df = pd.DataFrame(filtered)
        df.to_csv("product_prices.csv", index=False)
        print("📁 Saved to product_prices.csv")
        send_email(filtered, budget)
        print("📧 Email sent with deals.")
    else:
        print("❌ No deals found under your budget.")
