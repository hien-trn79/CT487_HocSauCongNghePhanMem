# ==============================================
# 📝 CODE SUMMARIZATION with Hugging Face Model
# ==============================================
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# 1️⃣ Tải model CodeT5 (được huấn luyện cho code summarization)
model_name = "Salesforce/codet5-small"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# 2️⃣ Input: code function
code = """
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
"""

# 3️⃣ Hàm sinh tóm tắt code


def generate_summary(code_text):
    inputs = tokenizer(code_text, return_tensors="pt", truncation=True)
    summary_ids = model.generate(inputs["input_ids"], max_length=50)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary


# 4️⃣ Gọi hàm và in kết quả
summary = generate_summary(code)

print("=== 🧾 Generated Comment ===")
print(summary)
