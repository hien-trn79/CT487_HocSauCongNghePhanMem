# Huấn luyện Random Forest với TF-IDF để so sánh
rf_tfidf = RandomForestClassifier(
n_estimators=100,

max_depth=10,
random_state=42
)
rf_tfidf.fit(X_train_tfidf, y_train)
y_pred_tfidf = rf_tfidf.predict(X_test_tfidf)
# Đánh giá
print("\nRandom Forest với TF-IDF:")
print(f"Accuracy: {accuracy_score(y_test, y_pred_tfidf):.4f}")
print(classification_report(y_test, y_pred_tfidf))
# Kết luận
print("\nSo sánh biểu diễn vector:")
print(f"SVM + TF-IDF: {accuracy_score(y_test,
svm_model.predict(X_test_tfidf)):.4f}")
print(f"RF + Word2Vec: {accuracy_score(y_test,
rf_model.predict(X_test_w2v)):.4f}")
print(f"RF + TF-IDF: {accuracy_score(y_test, y_pred_tfidf):.4f}")