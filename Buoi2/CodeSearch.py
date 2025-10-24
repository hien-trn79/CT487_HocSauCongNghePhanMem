# ==============================================
# 🔍 CODE SEARCH using Embeddings + Cosine Similarity
# ==============================================
from openai import OpenAI
import numpy as np

# 1️ Khởi tạo client
client = OpenAI(api_key="YOUR_API_KEY_HERE")

# 2️ Dữ liệu code database (các snippet cần tìm)
code_database = [
    {"code": "arr.sort()", "language": "python"},
    {"code": "Arrays.sort(arr)", "language": "java"},
    {"code": "sorted(arr)", "language": "python"},
    {"code": "arr = arr.sort(reverse=False)", "language": "python"},
    {"code": "sort_array(arr)", "language": "c++"}
]

# 3️ Hàm mã hóa chuỗi thành vector embedding


def encode(text):
    response = client.embeddings.create(
        model="text-embedding-3-small",  # mô hình embedding nhỏ và nhanh
        input=text
    )
    return np.array(response.data[0].embedding)

# 4️ Hàm tính cosine similarity


def cosine_similarity(vec, vecs):
    dot_products = np.dot(vecs, vec)
    norms = np.linalg.norm(vecs, axis=1) * np.linalg.norm(vec)
    return dot_products / norms

# 5️ Hàm tìm code tương tự nhất


def search_code(query, top_k=3):
    # Encode query và code
    query_vector = encode(query)
    code_vectors = np.array([encode(snippet["code"])
                            for snippet in code_database])

    # Tính độ tương tự
    similarities = cosine_similarity(query_vector, code_vectors)

    # Lấy top k kết quả
    top_indices = np.argsort(similarities)[::-1][:top_k]
    results = []
    for idx in top_indices:
        snippet = code_database[idx]
        results.append({
            "code": snippet["code"],
            "language": snippet["language"],
            "similarity": round(float(similarities[idx]), 3)
        })
    return results


# 6 Thử chạy với query
query = "sort array in ascending order"
results = search_code(query)

# 7 In kết quả
print("=== 🔍 Search Results ===")
for r in results:
    print(f"{r['language']:>7} | {r['code']:<25} | similarity: {r['similarity']}")
