import ast
import re
import os
import pandas as pd

# === HÀM TIỀN XỬ LÝ MÃ NGUỒN PYTHON ===
def preprocess_python_code(code):
    # Loại bỏ comment (cả dạng # và """ """)
    code = re.sub(r'#.*', '', code)
    code = re.sub(r'"""[\s\S]*?"""', '', code)
    code = re.sub(r"'''[\s\S]*?'''", '', code)
    # Chuẩn hóa khoảng trắng
    code = re.sub(r'\s+', ' ', code)
    return code.strip()


# === HÀM TRÍCH XUẤT CÁC HÀM (function) TRONG MÃ NGUỒN ===
def extract_functions(code):
    try:
        tree = ast.parse(code)
        functions = []

        # Duyệt qua cây cú pháp để tìm các hàm
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                func_code = ast.get_source_segment(code, node)
                functions.append({
                    'name': node.name,
                    'code': func_code,
                    'processed_code': preprocess_python_code(func_code)
                })

        return functions

    except SyntaxError:
        # Nếu file có lỗi cú pháp thì bỏ qua
        return []


# === PHẦN CHÍNH: ĐỌC FILE VÀ TRÍCH XUẤT HÀM ===
processed_data = []

for i in range(10):  # Cho 10 file đã tải về
    file_path = f"data/raw/file_{i}.py"

    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            code = f.read()

        # Tiền xử lý và trích xuất hàm
        functions = extract_functions(code)
        processed_data.extend(functions)

print(f"✅ Extracted {len(processed_data)} functions")

# === LƯU DỮ LIỆU ĐÃ XỬ LÝ RA CSV ===
os.makedirs("data/processed", exist_ok=True)
df = pd.DataFrame(processed_data)
df.to_csv("data/processed/functions.csv", index=False)
print("💾 Saved processed data → data/processed/functions.csv")
