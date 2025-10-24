# 🔧 Program Repair
# Tình huống: Tự động sửa lỗi syntax trong code Python

# =========================
# 📥 Input: Buggy code
# =========================
buggy_code = """
def factorial(n):
    if n = 1:  # Bug: should be == not =
        return 1
    else:
        return n * factorial(n-1)
"""

# =========================
# ⚙️ Deep Learning Model: Sequence-to-sequence transformer (mô phỏng)
# =========================


def tokenize(code):
    """
    Giả lập bước tokenization - tách code thành các token.
    """
    return code.replace("(", " ( ").replace(")", " ) ").replace(":", " :").split()


def detokenize(tokens):
    """
    Giả lập bước detokenization - ghép token lại thành code.
    """
    return " ".join(tokens).replace(" ( ", "(").replace(" )", ")").replace(" :", ":")


def transformer_model_generate(tokens):
    """
    Mô phỏng mô hình transformer sửa lỗi cú pháp.
    - Nếu phát hiện "=" nằm trong điều kiện 'if', đổi thành "==".
    """
    fixed_tokens = []
    for i in range(len(tokens)):
        if tokens[i] == "=" and tokens[i - 1] == "n" and tokens[i - 2] == "if":
            fixed_tokens.append("==")
        else:
            fixed_tokens.append(tokens[i])
    return fixed_tokens

# =========================
# 🧠 Program Repair Pipeline
# =========================


def repair_code(buggy_code):
    tokens = tokenize(buggy_code)
    fixed_tokens = transformer_model_generate(tokens)
    fixed_code = detokenize(fixed_tokens)
    return fixed_code


# =========================
# 📤 Output: Repaired code & analysis
# =========================
fixed_code = repair_code(buggy_code)

repair_result = {
    "original_error": "SyntaxError: invalid syntax",
    "fix_applied": "Changed assignment operator '=' to comparison operator '=='",
    "confidence": 0.94
}

# =========================
# 🧾 Print result
# =========================
print("🐞 Original Buggy Code:")
print(buggy_code)
print("\n✅ Repaired Code:")
print(fixed_code)
print("\n📊 Repair Result:")
for k, v in repair_result.items():
    print(f"- {k}: {v}")
