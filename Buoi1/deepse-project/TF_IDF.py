import os
import pickle
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# === 1. ĐỌC DỮ LIỆU ĐÃ XỬ LÝ ===
df = pd.read_csv("data/processed/functions.csv")
print(f"✅ Đọc thành công {len(df)} hàm từ file CSV")

# === 2. KHỞI TẠO TF-IDF VECTORIZER ===
tfidf = TfidfVectorizer(
    max_features=5000,       # Giới hạn số lượng từ
    ngram_range=(1, 3),      # Sử dụng unigram, bigram, trigram
    stop_words='english'     # Loại bỏ stopwords tiếng Anh
)

# === 3. TẠO MA TRẬN TF-IDF ===
tfidf_matrix = tfidf.fit_transform(df['processed_code'])

# === 4. CHUYỂN THÀNH DATAFRAME (để dễ quan sát hoặc debug) ===
tfidf_df = pd.DataFrame(
    tfidf_matrix.toarray(),
    columns=tfidf.get_feature_names_out()
)

print(f"✅ Shape of TF-IDF matrix: {tfidf_matrix.shape}")
print(tfidf_df.head())

# === 5. LƯU MÔ HÌNH VECTORIZER ĐỂ TÁI SỬ DỤNG ===
os.makedirs("models", exist_ok=True)

with open("models/tfidf_vectorizer.pkl", "wb") as f:
    pickle.dump(tfidf, f)
print("💾 Đã lưu model vectorizer → models/tfidf_vectorizer.pkl")

# === 6. LƯU MA TRẬN TF-IDF ===
os.makedirs("data/processed", exist_ok=True)

np.save("data/processed/tfidf_matrix.npy", tfidf_matrix.toarray())
print("💾 Đã lưu TF-IDF matrix → data/processed/tfidf_matrix.npy")
