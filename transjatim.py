import pandas as pd
import numpy as np
import re
import string
from google_play_scraper import reviews, Sort
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

# Scraping review dari aplikasi TransJatim Ajaib
app_id = 'ngi.muchi.jatimajaib'
print(f"🔍 Mengambil review dari aplikasi: {app_id}")
result, _ = reviews(app_id, lang='id', country='id', count=1000, sort=Sort.NEWEST)

if not result:
    print("❌ Tidak ada review ditemukan.")
    exit()

df = pd.DataFrame(result)

# Ambil kolom isi komentar
if 'content' in df.columns:
    df['ulasan'] = df['content']
elif 'review' in df.columns:
    df['ulasan'] = df['review']
else:
    print('❌ Kolom ulasan tidak ditemukan di data.')
    exit()

df = df[['ulasan']].dropna().reset_index(drop=True)

# Normalisasi slang dan stemming
slang_dict = {"bgt": "banget", "gpp": "tidak apa-apa", "jd": "jadi", "kmu": "kamu", "aq": "aku", "gw": "saya"}
stemmer = StemmerFactory().create_stemmer()

def clean_text(text):
    text = text.lower()
    text = re.sub(r'\d+', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = ' '.join([slang_dict.get(word, word) for word in text.split()])
    text = stemmer.stem(text)
    return text

df['clean_ulasan'] = df['ulasan'].apply(clean_text)

# Simpan semua ke file
output_file = 'transjatim_comments.csv'
df[['ulasan', 'clean_ulasan']].to_csv(output_file, index=False)
print(f"✅ Disimpan ke file: {output_file}")
