# ==============================================
# 🔄 SOFTWARE REFACTORING (AI-based Code Smell Detection)
# ==============================================
import ast
import random

# Giả lập các module AI


class DummyCNNModel:
    """Giả lập mô hình CNN dự đoán code smell"""

    def predict(self, features):
        # Trả về xác suất ngẫu nhiên mô phỏng
        return {
            "long_method": round(random.uniform(0.8, 0.99), 2),
            "god_class": round(random.uniform(0.1, 0.4), 2)
        }


cnn_model = DummyCNNModel()

# 1️⃣ Input: Code có vấn đề
code = """
class DataProcessor:
    def process_data(self, data):
        # Long method with multiple responsibilities
        # Validate data
        if not data:
            raise ValueError("Data is empty")
        if not isinstance(data, list):
            raise TypeError("Data must be a list")
        # Process data
        cleaned_data = []
        for item in data:
            if item is not None:
                cleaned_data.append(item.strip().lower())
        # Save to database
        database.save(cleaned_data)
        # Send notification
        notification_service.send("Data processed")
        return cleaned_data
"""

# 2️⃣ Hàm trích đặc trưng từ mã nguồn (giả lập)


def extract_features(code_ast):
    """Phân tích code AST và trích feature cho mô hình"""
    num_lines = len(ast.dump(code_ast))
    num_methods = sum(isinstance(n, ast.FunctionDef)
                      for n in ast.walk(code_ast))
    num_comments = code.count("#")
    return [num_lines, num_methods, num_comments]

# 3️⃣ Hàm phát hiện code smell


def detect_code_smells(code_text):
    code_ast = ast.parse(code_text)
    features = extract_features(code_ast)
    prediction = cnn_model.predict(features)

    # Giả định nếu xác suất long_method > 0.9 thì có mùi code
    smells = {
        "long_method": prediction["long_method"],
        "god_class": prediction["god_class"],
        "refactoring_suggestion": "Extract methods for validation, processing, and persistence"
    }
    return smells

# 4️⃣ Hàm sinh gợi ý refactor


def generate_refactoring_suggestions(smell_info):
    suggestions = []
    if smell_info["long_method"] > 0.9:
        suggestions.extend([
            "Extract validate_data() method",
            "Extract clean_data() method",
            "Extract save_and_notify() method"
        ])
    if smell_info["god_class"] > 0.8:
        suggestions.append("Split class into smaller, cohesive classes")
    return suggestions


# 5️⃣ Thực thi
smells = detect_code_smells(code)
suggestions = generate_refactoring_suggestions(smells)

# 6️⃣ Kết quả
print("=== 🔍 Detected Code Smells ===")
for k, v in smells.items():
    if k != "refactoring_suggestion":
        print(f"{k}: {v}")
print("Refactoring Suggestion:", smells["refactoring_suggestion"])

print("\n=== 🛠️ Suggested Refactorings ===")
for s in suggestions:
    print("-", s)
