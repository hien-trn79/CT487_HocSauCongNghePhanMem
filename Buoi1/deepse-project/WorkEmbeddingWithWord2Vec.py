import os
import numpy as np
import gensim
from gensim.models import Word2Vec
import nltk
from nltk.tokenize import word_tokenize
import pandas as pd

# === 1. ĐỌC DỮ LIỆU ĐÃ XỬ LÝ ===
df = pd.read_csv("data/processed/functions.csv")
print(f"✅ Đọc thành công {len(df)} hàm từ file CSV")

# === 2. TẢI TOKENIZER NLTK ===
nltk.download('punkt')

# === 3. CHUẨN BỊ DỮ LIỆU CHO WORD2VEC ===
tokenized_code = []
for code in df['processed_code']:
    tokens = word_tokenize(code)
    tokenized_code.append(tokens)

print(f"✅ Đã token hóa {len(tokenized_code)} đoạn code")

# === 4. HUẤN LUYỆN MÔ HÌNH WORD2VEC ===
w2v_model = Word2Vec(
    sentences=tokenized_code,
    vector_size=100,   # Kích thước vector
    window=5,          # Cửa sổ ngữ cảnh
    min_count=2,       # Tối thiểu số lần xuất hiện của từ
    workers=4          # Số luồng xử lý song song
)

# === 5. LƯU MÔ HÌNH WORD2VEC ===
os.makedirs("models", exist_ok=True)
w2v_model.save("models/w2v_code.model")
print("💾 Đã lưu mô hình Word2Vec → models/w2v_code.model")

# === 6. TẠO VECTOR ĐẠI DIỆN CHO MỖI HÀM ===
def create_document_vector(doc_tokens, model):
    """Tạo vector đại diện cho hàm bằng trung bình vector của các token."""
    doc_vector = []
    for token in doc_tokens:
        if token in model.wv:
            doc_vector.append(model.wv[token])
    if not doc_vector:
        return np.zeros(model.vector_size)
    return np.mean(doc_vector, axis=0)

# === 7. TẠO EMBEDDING CHO MỖI HÀM ===
doc_vectors = []
for tokens in tokenized_code:
    doc_vectors.append(create_document_vector(tokens, w2v_model))

# === 8. LƯU CÁC VECTOR RA FILE ===
os.makedirs("data/processed", exist_ok=True)
doc_vectors_array = np.array(doc_vectors)
np.save("data/processed/w2v_vectors.npy", doc_vectors_array)
print(f"✅ Shape of Word2Vec embeddings: {doc_vectors_array.shape}")
print("💾 Đã lưu Word2Vec vectors → data/processed/w2v_vectors.npy")
