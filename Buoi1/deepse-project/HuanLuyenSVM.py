from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score
# Mô hình SVM
svm_model = SVC(kernel='linear', C=1.0, random_state=42)
svm_model.fit(X_train_tfidf, y_train)
# Dự đoán
y_pred = svm_model.predict(X_test_tfidf)
# Đánh giá
print("SVM với TF-IDF:")
print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
print(classification_report(y_test, y_pred))
# Lưu mô hình
import pickle
with open("models/svm_tfidf.pkl", "wb") as f:
    pickle.dump(svm_model, f)