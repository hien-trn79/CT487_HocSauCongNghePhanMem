# 🧭 Fault Localization
# Tình huống: Định vị lỗi từ test cases thất bại

# =========================
# Input: Test execution data
# =========================
test_results = {
    "passed_tests": ["test_add", "test_subtract"],
    "failed_tests": ["test_multiply", "test_divide"],
    "coverage_matrix": {
        # [test_add, test_subtract, test_multiply, test_divide]
        "line_1": [1, 1, 1, 0],
        "line_5": [0, 0, 1, 1],
        "line_8": [1, 1, 1, 1],
        "line_12": [0, 0, 0, 1]
    }
}

# =========================
# Deep Learning Model: CNN on coverage matrix (giả lập)
# =========================


def create_feature_matrix(coverage_data):
    """
    Biến đổi coverage matrix thành feature matrix cho mô hình.
    """
    feature_matrix = []
    for line, coverage in coverage_data.items():
        feature_matrix.append({
            "line": int(line.split("_")[1]),
            "coverage_vector": coverage
        })
    return feature_matrix


def cnn_model_predict(features):
    """
    Giả lập mô hình CNN dự đoán độ nghi ngờ (suspiciousness) cho từng dòng.
    Ở thực tế, CNN sẽ học từ coverage matrix và nhãn lỗi để xác định dòng khả nghi.
    """
    # Ví dụ: mô phỏng độ nghi ngờ dựa trên mức độ liên quan với test thất bại
    suspicious_scores = []
    for f in features:
        # Càng liên quan nhiều đến test thất bại thì điểm càng cao
        suspiciousness = (f["coverage_vector"][2] +
                          f["coverage_vector"][3]) / 2
        suspicious_scores.append({
            "line": f["line"],
            "suspiciousness": round(suspiciousness * 0.95, 2)
        })
    # Sắp xếp theo độ nghi ngờ giảm dần
    suspicious_scores.sort(key=lambda x: x["suspiciousness"], reverse=True)
    return suspicious_scores

# =========================
# Fault Localization Pipeline
# =========================


def localize_fault(coverage_data, test_results):
    features = create_feature_matrix(coverage_data)
    suspiciousness_scores = cnn_model_predict(features)
    return suspiciousness_scores


# =========================
# Output: Ranked suspicious lines
# =========================
fault_localization = localize_fault(
    test_results["coverage_matrix"], test_results)

print("🔍 Fault Localization Result:")
for item in fault_localization:
    print(f"➡️ Line {item['line']} — Suspiciousness: {item['suspiciousness']}")
