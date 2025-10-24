# Developer Collaboration
# Tình huống: Gợi ý code reviewer phù hợp cho Pull Request (PR)

# =========================
# Input: Pull request information
# =========================
import random
pull_request = {
    "files_changed": [
        "src/authentication/oauth.py",
        "src/database/user_model.py",
        "tests/test_auth.py"
    ],
    "lines_added": 145,
    "lines_deleted": 23,
    "description": "Implement OAuth2 authentication with Google",
    "author": "alice.smith"
}

# =========================
# Deep Learning Model: Graph Neural Network (mô phỏng)
# =========================

# Mô phỏng cơ sở dữ liệu chuyên môn của các developer
developer_expertise = {
    "bob.johnson@company.com": ["authentication", "security", "oauth"],
    "carol.white@company.com": ["database", "backend", "orm"],
    "david.lee@company.com": ["frontend", "ui", "vue"],
    "emma.nguyen@company.com": ["testing", "pytest", "automation"],
}


def build_expertise_graph():
    """
    Giả lập đồ thị chuyên môn của developer.
    Mỗi node là developer, các cạnh thể hiện mối quan hệ cộng tác (collaboration).
    """
    print("Building developer expertise graph...")
    graph = {
        "nodes": list(developer_expertise.keys()),
        "edges": [
            ("bob.johnson@company.com", "carol.white@company.com"),
            ("carol.white@company.com", "emma.nguyen@company.com"),
            ("david.lee@company.com", "emma.nguyen@company.com"),
        ]
    }
    return graph


def extract_tech_features(files):
    """
    Trích xuất đặc trưng công nghệ từ danh sách file thay đổi trong PR.
    """
    tech_keywords = []
    for f in files:
        if "auth" in f.lower():
            tech_keywords.append("authentication")
        if "oauth" in f.lower():
            tech_keywords.append("oauth")
        if "database" in f.lower() or "model" in f.lower():
            tech_keywords.append("database")
        if "test" in f.lower():
            tech_keywords.append("testing")
    print(f"Extracted tech features: {tech_keywords}")
    return tech_keywords


def gnn_model_predict(graph, tech_features):
    """
    Giả lập GNN đánh giá điểm chuyên môn giữa developer và PR.
    """
    scores = {}
    for dev, skills in developer_expertise.items():
        overlap = len(set(skills) & set(tech_features))
        score = 0.6 + 0.1 * overlap + random.uniform(0, 0.2)
        scores[dev] = round(min(score, 1.0), 2)
    return scores


def top_reviewers(scores, top_k=2):
    """
    Lấy ra top K reviewer có điểm cao nhất.
    """
    sorted_devs = sorted(
        scores.items(), key=lambda x: x[1], reverse=True)[:top_k]
    recommendations = []
    for dev, score in sorted_devs:
        domain = ", ".join(developer_expertise[dev]).title()
        recommendations.append({
            "developer": dev,
            "expertise_score": score,
            "previous_reviews": random.randint(10, 25),
            "domain": domain
        })
    return recommendations

# =========================
# Recommendation pipeline
# =========================


def recommend_reviewers(pr_info):
    dev_graph = build_expertise_graph()
    tech_features = extract_tech_features(pr_info["files_changed"])
    reviewer_scores = gnn_model_predict(dev_graph, tech_features)
    return top_reviewers(reviewer_scores)


# =========================
# Output: Recommended reviewers
# =========================
recommendations = recommend_reviewers(pull_request)

# =========================
# Print results
# =========================
print("\nPull Request Summary:")
for k, v in pull_request.items():
    print(f"- {k}: {v}")

print("\nRecommended Reviewers:")
for r in recommendations:
    print(f"- {r['developer']} | Score: {r['expertise_score']} | Domain: {r['domain']} | Reviews: {r['previous_reviews']}")
