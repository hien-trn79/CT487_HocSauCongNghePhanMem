# ======================================================
# 🔍 BUG FINDING using GNN-based Vulnerability Detection
# ======================================================

import networkx as nx
import random

# === Input: C code snippet ===
c_code = """
void copy_string(char *dest, char *src) {
    while (*src) {
        *dest++ = *src++; // Potential buffer overflow
    }
    *dest = '\\0';
}
"""

# === 1️ Parse to Control Flow Graph (CFG) ===


def parse_to_cfg(code):
    """
    Giả lập việc chuyển code C thành Control Flow Graph.
    Thực tế dùng công cụ như Joern, CodeQL, hay LLVM.
    """
    cfg = nx.DiGraph()
    # Các node đại diện cho dòng code
    cfg.add_nodes_from([
        (1, {"code": "void copy_string(char *dest, char *src) {"}),
        (2, {"code": "while (*src) {"}),
        (3, {"code": "*dest++ = *src++; // Potential buffer overflow"}),
        (4, {"code": "}"}),
        (5, {"code": "*dest = '\\0';"}),
        (6, {"code": "}"})
    ])
    # Các cạnh biểu diễn luồng điều khiển
    cfg.add_edges_from([
        (1, 2), (2, 3), (3, 2), (2, 4), (4, 5), (5, 6)
    ])
    return cfg

# === 2️ Giả lập GNN phân tích đồ thị ===


def gnn_model_predict(cfg):
    """
    Mô phỏng mô hình GNN học trên CFG.
    Ở đây, nó sẽ "học" được rằng dòng có phép gán con trỏ là nguy hiểm.
    """
    vulnerable_nodes = []
    for node, data in cfg.nodes(data=True):
        code_line = data["code"]
        # Phát hiện pattern nguy hiểm
        if "*dest++ = *src++" in code_line:
            vulnerable_nodes.append({
                "node": node,
                "vulnerability_type": "Buffer Overflow",
                "severity": "HIGH",
                "description": "No bounds checking on destination buffer",
                "fix_suggestion": "Add length parameter and check bounds"
            })
    return vulnerable_nodes

# === 3️ Kết hợp lại thành pipeline hoàn chỉnh ===


def find_bugs(code):
    cfg = parse_to_cfg(code)
    vulnerability_nodes = gnn_model_predict(cfg)
    return vulnerability_nodes


# === 4️ Gọi model để phân tích ===
bug_report = find_bugs(c_code)

# === 5️ In kết quả ===
print("=== 🧾 BUG REPORT ===")
for bug in bug_report:
    print(f"Vulnerability: {bug['vulnerability_type']}")
    print(f"Location: Line {bug['node']}: {c_code.splitlines()[bug['node']]}")
    print(f"Severity: {bug['severity']}")
    print(f"Description: {bug['description']}")
    print(f"Fix Suggestion: {bug['fix_suggestion']}")
    print("----------------------------------------------------")
