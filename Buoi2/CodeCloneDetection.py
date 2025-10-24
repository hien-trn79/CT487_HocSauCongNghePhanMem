# ==============================================
# 🎯 CODE CLONE DETECTION (AI-based - Siamese Network)
# ==============================================
import ast
import math
import random

# Giả lập các thành phần học sâu


def parse_to_ast(code):
    """Chuyển code thành cây cú pháp (AST)"""
    return ast.parse(code)


def ast_encoder(ast_tree):
    """Mã hóa AST thành vector đặc trưng (embedding)"""
    # Giả lập embedding: vector 5 chiều
    num_nodes = len(list(ast.walk(ast_tree)))
    num_functions = sum(isinstance(n, ast.FunctionDef)
                        for n in ast.walk(ast_tree))
    num_returns = sum(isinstance(n, ast.Return) for n in ast.walk(ast_tree))
    num_ops = sum(isinstance(n, ast.BinOp) for n in ast.walk(ast_tree))
    num_names = sum(isinstance(n, ast.Name) for n in ast.walk(ast_tree))
    return [num_nodes, num_functions, num_returns, num_ops, num_names]


def siamese_network(embed1, embed2):
    """Tính độ tương đồng cosine giữa hai embedding"""
    dot = sum(a*b for a, b in zip(embed1, embed2))
    norm1 = math.sqrt(sum(a*a for a in embed1))
    norm2 = math.sqrt(sum(b*b for b in embed2))
    similarity = dot / (norm1 * norm2 + 1e-8)
    return round(similarity, 2)


# Input
code1 = """
def calculate_area(length, width):
    return length * width
"""

code2 = """
def compute_rectangle_area(l, w):
    area = l * w
    return area
"""

# Deep Learning Model pipeline


def detect_clones(code1, code2):
    ast1 = parse_to_ast(code1)
    ast2 = parse_to_ast(code2)

    embed1 = ast_encoder(ast1)
    embed2 = ast_encoder(ast2)

    similarity_score = siamese_network(embed1, embed2)

    # Dựa theo ngưỡng để xác định clone
    is_clone = similarity_score > 0.8
    clone_type = "Type-2" if is_clone else "Not Clone"

    return {
        "similarity_score": similarity_score,
        "clone_type": clone_type,
        "is_clone": is_clone
    }


# Output
result = detect_clones(code1, code2)

print("=== 🎯 CODE CLONE DETECTION RESULT ===")
print("Similarity Score:", result["similarity_score"])
print("Clone Type:", result["clone_type"])
print("Is Clone:", result["is_clone"])
