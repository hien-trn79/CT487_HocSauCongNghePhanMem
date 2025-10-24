# ======================================================
# 🐛 SOFTWARE DEFECT PREDICTION (AI-based simulation)
# ======================================================
import numpy as np

# === Input: Code metrics ===
file_metrics = {
    "lines_of_code": 450,
    "cyclomatic_complexity": 12,
    "number_of_methods": 8,
    "coupling_between_objects": 5,
    "weighted_methods_per_class": 25,
    "code_churn": 0.3,          # Tỷ lệ thay đổi gần đây
    "developer_experience": 2.5  # Năm kinh nghiệm lập trình viên
}

# === Chuẩn hóa dữ liệu ===


def normalize(metrics):
    # Chuyển thành vector numpy
    values = np.array(list(metrics.values()), dtype=float)

    # Min-max normalization (giả lập)
    min_vals = np.array([0, 1, 1, 0, 0, 0, 0])
    max_vals = np.array([1000, 20, 20, 15, 50, 1, 10])
    normalized = (values - min_vals) / (max_vals - min_vals)

    return normalized

# === Giả lập mô hình Deep Neural Network ===


def dnn_model_predict(normalized_features):
    # Mô phỏng các trọng số mạng nơ-ron
    weights = np.array([0.2, 0.3, 0.15, 0.1, 0.1, 0.1, -0.05])
    bias = 0.1

    # Tính đầu ra (sigmoid)
    z = np.dot(normalized_features, weights) + bias
    probability = 1 / (1 + np.exp(-z))

    return round(float(probability), 2)

# === Hàm chính: Dự đoán khả năng lỗi ===


def predict_defect_probability(metrics):
    normalized = normalize(metrics)
    probability = dnn_model_predict(normalized)

    # Đánh giá mức độ rủi ro
    if probability >= 0.7:
        risk = "HIGH"
        rec = "Increase code review and testing for this file."
    elif probability >= 0.4:
        risk = "MEDIUM"
        rec = "Consider static analysis or pair programming."
    else:
        risk = "LOW"
        rec = "Normal maintenance suffices."

    return {
        "defect_probability": probability,
        "risk_level": risk,
        "recommendation": rec
    }


# === Output ===
prediction = predict_defect_probability(file_metrics)

print("=== 🧾 SOFTWARE DEFECT PREDICTION RESULT ===")
for k, v in prediction.items():
    print(f"{k}: {v}")
