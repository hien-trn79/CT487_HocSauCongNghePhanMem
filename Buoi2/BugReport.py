# Bug Report Management
# Tình huống: Phân loại và phân công bug reports tự động

# =========================
# Input: Bug report
# =========================
import random
bug_report = {
    "title": "Application crashes when uploading large files",
    "description": (
        "When I try to upload files larger than 100MB, the app freezes and crashes. "
        "This happens consistently on Chrome browser."
    ),
    "steps": "1. Click upload button 2. Select file >100MB 3. App crashes",
    "environment": "Chrome 91, Windows 10"
}

# =========================
# Deep Learning Model: BERT for classification (mô phỏng)
# =========================


def bert_encoder(text):
    """
    Giả lập bộ mã hóa BERT để trích xuất vector đặc trưng ngữ nghĩa từ văn bản bug report.
    """
    print(f"🔍 Encoding text using BERT: {text[:60]}...")
    return [random.random() for _ in range(768)]  # vector 768 chiều mô phỏng


def severity_classifier(features):
    """
    Phân loại mức độ nghiêm trọng (severity) dựa trên đặc trưng văn bản.
    """
    keywords = ["crash", "error", "fail", "freeze"]
    return "HIGH" if any(k in bug_report["description"].lower() for k in keywords) else "MEDIUM"


def component_classifier(features):
    """
    Xác định module hoặc thành phần bị lỗi.
    """
    if "upload" in bug_report["description"].lower():
        return "File Upload Module"
    elif "login" in bug_report["description"].lower():
        return "Authentication Module"
    elif "database" in bug_report["description"].lower():
        return "Database Layer"
    else:
        return "Unknown Component"


def developer_recommender(features):
    """
    Gợi ý lập trình viên phụ trách sửa lỗi dựa trên component.
    """
    mapping = {
        "File Upload Module": "john.doe@company.com",
        "Authentication Module": "alice.nguyen@company.com",
        "Database Layer": "minh.tran@company.com",
        "Unknown Component": "team_lead@company.com"
    }
    comp = component_classifier(features)
    return mapping.get(comp, "team_lead@company.com")

# =========================
# Bug classification pipeline
# =========================


def classify_bug_report(report):
    # Encode mô phỏng bằng BERT
    text_features = bert_encoder(report["description"])

    # Multi-task classification
    severity = severity_classifier(text_features)
    component = component_classifier(text_features)
    developer = developer_recommender(text_features)

    # Thêm một số giá trị mô phỏng
    classification = {
        "severity": severity,
        "component": component,
        "assigned_developer": developer,
        "estimated_fix_time": "3-5 days" if severity == "HIGH" else "1-2 days",
        "duplicate_probability": round(random.uniform(0.05, 0.25), 2)
    }
    return classification


# =========================
# Output: Classified and assigned bug
# =========================
classification = classify_bug_report(bug_report)

# =========================
# Print result
# =========================
print("\n🐞 Bug Report Input:")
for k, v in bug_report.items():
    print(f"- {k}: {v}")

print("\n✅ Classification Result:")
for k, v in classification.items():
    print(f"- {k}: {v}")
