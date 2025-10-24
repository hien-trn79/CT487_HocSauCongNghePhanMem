# ==============================================
# 💻 Code Generation from Natural Language
# Using GPT-based model (e.g., GPT-4 / GPT-5)
# ==============================================

from openai import OpenAI

# 1️⃣ Khởi tạo client (nhớ đặt API key của bạn)
client = OpenAI(api_key="YOUR_API_KEY_HERE")

# 2️⃣ Input: mô tả tự nhiên
description = "Create a function that finds the maximum element in a list"

# 3️⃣ Hàm sinh code từ mô tả


def generate_code(description):
    prompt = f"Write Python code for this instruction:\n\n{description}\n\nCode:"

    response = client.chat.completions.create(
        model="gpt-4o-mini",  # hoặc "gpt-4o", "gpt-5"
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    generated_code = response.choices[0].message.content
    return generated_code


# 4️⃣ Gọi hàm và in kết quả
generated_code = generate_code(description)

print("=== 🧾 Generated Code ===")
print(generated_code)
