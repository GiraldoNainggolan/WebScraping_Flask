import pandas as pd
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
# options.add_argument("--headless")  # Aktifkan jika mau tanpa GUI
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--lang=id")
options.add_argument("start-maximized")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

video_urls = [
    'https://www.youtube.com/watch?v=aA98ajOleo0',
    'https://www.youtube.com/watch?v=yIPZQfbVnbg',
    'https://www.youtube.com/watch?v=6OK_-1W7OO0',
    'https://www.youtube.com/watch?v=-rLCbCZoI3k'
]

all_comments = []

for url in video_urls:
    print(f"\n🔍 Scraping komentar dari: {url}")
    driver.get(url)
    time.sleep(5)

    # Tutup popup consent jika muncul
    try:
        consent = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Setuju")] | //button[contains(text(), "I Agree")]'))
        )
        consent.click()
        print("✅ Popup consent ditutup.")
    except:
        pass  # Tidak ada popup

    # Scroll beberapa kali
    for _ in range(10):
        driver.execute_script("window.scrollBy(0, 1000);")
        time.sleep(1)

    comments = driver.find_elements(By.XPATH, '//*[@id="content-text"]')
    video_comments = [comment.text for comment in comments if comment.text.strip()]
    print(f"✅ Komentar diambil: {len(video_comments)}")

    all_comments.extend({'video_url': url, 'comment': c} for c in video_comments)

driver.quit()

# Simpan semua komentar ke CSV
df = pd.DataFrame(all_comments)
output_file = 'youtube_comments.csv'
df.to_csv(output_file, index=False)
print(f"\n✅ Semua komentar disimpan ke file: {output_file}")
