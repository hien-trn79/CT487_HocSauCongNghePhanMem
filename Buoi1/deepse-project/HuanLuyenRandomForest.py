from sklearn.ensemble import RandomForestClassifier
# Mô hình Random Forest
rf_model = RandomForestClassifier(
n_estimators=100,
max_depth=10,
random_state=42
)
rf_model.fit(X_train_w2v, y_train)
# Dự đoán
y_pred = rf_model.predict(X_test_w2v)
# Đánh giá
print("\nRandom Forest với Word2Vec:")
print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
print(classification_report(y_test, y_pred))
# Lưu mô hình
with open("models/rf_w2v.pkl", "wb") as f:
    pickle.dump(rf_model, f)