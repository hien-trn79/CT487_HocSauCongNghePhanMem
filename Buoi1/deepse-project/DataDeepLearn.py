import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

# Đọc dữ liệu vector
tfidf_vectors = np.load("data/processed/tfidf_matrix.npy")
w2v_vectors = np.load("data/processed/w2v_vectors.npy")

# Đọc file chứa thông tin hàm
df = pd.read_csv("data/processed/functions.csv")

# Hàm gán nhãn cho mỗi hàm
def assign_label(func_name):
    if func_name.startswith(('get_', 'fetch_')):
        return 0
    elif func_name.startswith(('create_', 'build_')):
        return 1
    else:
        return 2

# Thêm cột nhãn vào DataFrame
df['label'] = df['name'].apply(assign_label)

# Chia dữ liệu TF-IDF thành train/test
X_train_tfidf, X_test_tfidf, y_train, y_test = train_test_split(
    tfidf_vectors, df['label'], test_size=0.3, random_state=42
)

# Chia dữ liệu Word2Vec tương ứng
X_train_w2v, X_test_w2v, _, _ = train_test_split(
    w2v_vectors, df['label'], test_size=0.3, random_state=42
)

print("TF-IDF train shape:", X_train_tfidf.shape)
print("TF-IDF test shape:", X_test_tfidf.shape)
print("Word2Vec train shape:", X_train_w2v.shape)
print("Word2Vec test shape:", X_test_w2v.shape)
print("Sample labels:", df['label'].value_counts())
