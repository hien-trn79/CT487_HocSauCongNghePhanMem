# ==============================================
# 📋 Requirements Engineering from User Reviews
# Using a BERT-based text classification pipeline
# ==============================================

# 1️⃣ Import libraries
from transformers import pipeline

# 2️⃣ Load pre-trained BERT model for text classification
# (ở đây dùng mô hình tổng quát, bạn có thể thay bằng mô hình đã fine-tune riêng)
classifier = pipeline("zero-shot-classification",
                      model="facebook/bart-large-mnli")

# 3️⃣ Input: user review
review = """
The app crashes when I try to upload large photos.
Please add batch upload feature and fix the memory issue.
"""

# 4️⃣ Hàm trích xuất yêu cầu từ review


def extract_requirements(review_text):
    # Các loại ý định (intents) cần phân loại
    candidate_labels = ["bug report", "feature request", "improvement"]

    # Tách câu trong review (đơn giản hóa)
    sentences = [s.strip() for s in review_text.split(".") if s.strip()]

    results = {}
    for sentence in sentences:
        # Phân loại từng câu xem là bug / feature / improvement
        classification = classifier(sentence, candidate_labels)
        intent = classification["labels"][0]  # Nhãn có xác suất cao nhất
        results[intent] = sentence

    return results


# 5️⃣ Gọi hàm trích xuất
intentions = extract_requirements(review)

print("=== Extracted Intentions ===")
for key, value in intentions.items():
    print(f"{key}: {value}")

# 6️⃣ Chuyển sang dạng yêu cầu có cấu trúc


def structure_requirements(intentions):
    functional = []
    non_functional = []
    priority = "medium"

    for intent, text in intentions.items():
        if intent == "feature request":
            functional.append("Batch upload photos")
            priority = "high"
        elif intent == "bug report":
            non_functional.append("Handle large files without crashing")
            priority = "high"
        elif intent == "improvement":
            non_functional.append("Fix memory issue")

    return {
        "functional": functional,
        "non_functional": non_functional,
        "priority": priority
    }


requirements = structure_requirements(intentions)

print("\n=== Structured Requirements ===")
for k, v in requirements.items():
    print(f"{k}: {v}")
