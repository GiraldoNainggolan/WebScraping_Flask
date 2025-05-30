# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# import time
# import pandas as pd

# # Setup Chrome options
# options = Options()
# # options.add_argument("--headless")  # Uncomment for headless mode
# options.add_argument("--disable-gpu")
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-dev-shm-usage")

# # Initialize the driver
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# # List of YouTube video URLs
# video_urls = [
#     'https://www.youtube.com/watch?v=aA98ajOleo0'  # Test with one URL first
# ]

# all_comments = []

# for url in video_urls:
#     print(f"📽️ Memproses video: {url}")
#     driver.get(url)
#     time.sleep(5)  # Wait for the page to load

#     # Scroll to load comments
#     for _ in range(5):  # Reduced scrolls for testing
#         driver.execute_script("window.scrollBy(0, 1000);")
#         time.sleep(2)

#     # Find comment elements
#     comments = driver.find_elements(By.CSS_SELECTOR, 'ytd-comment-thread-renderer')
#     print(f"✅ Komentar diambil: {len(comments)}")

#     for comment in comments:
#         try:
#             comment_text = comment.find_element(By.ID, 'content-text').text
#             all_comments.append({'video_url': url, 'comment': comment_text})
#         except Exception as e:
#             print(f"Error extracting comment: {e}")

# # Close the driver
# driver.quit()

# # Save to CSV
# if all_comments:
#     df = pd.DataFrame(all_comments)
#     df.to_csv('youtube_comments.csv', index=False, encoding='utf-8')
#     print(f"✅ Semua komentar disimpan ke file: youtube_comments.csv")
# else:
#     print("❌ Tidak ada komentar yang diambil.")