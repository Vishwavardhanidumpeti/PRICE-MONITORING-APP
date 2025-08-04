from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
import time

def search_amazon(query):
    options = Options()
    options.add_argument("--headless")  # Run browser in background
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.get("https://www.amazon.in")
    time.sleep(2)

    search_box = driver.find_element(By.ID, "twotabsearchtextbox")
    search_box.send_keys(query)
    search_box.submit()
    time.sleep(3)

    products = []
    results = driver.find_elements(By.XPATH, "//div[@data-component-type='s-search-result']")
    print(f"📦 Amazon found {len(results)} results")

    for item in results[:10]:  
        try:
            name = item.find_element(By.TAG_NAME, 'h2').text
            price = item.find_element(By.CSS_SELECTOR, ".a-price-whole").text.replace(",", "").strip()
            url = item.find_element(By.TAG_NAME, 'a').get_attribute("href")

            products.append({
                'website': 'Amazon',
                'name': name,
                'price': float(price),
                'url': url  
            })
        except Exception as e:
            print("❌ Amazon item skipped:", e)
            continue

    driver.quit()
    return products
