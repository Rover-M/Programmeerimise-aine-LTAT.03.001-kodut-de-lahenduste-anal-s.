import ast
import keyword
from difflib import SequenceMatcher


def read_file_content(path):
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()


def safe_percentage(value):
    return f"{round(value * 100)}%"


def text_similarity(text_a, text_b):
    forward = SequenceMatcher(None, text_a, text_b).ratio()
    backward = SequenceMatcher(None, text_b, text_a).ratio()
    return (forward + backward) / 2


def preprocess_raw_code(code):
    lines = [line.rstrip() for line in code.splitlines()]
    filtered = [line for line in lines if line.strip()]
    return "\n".join(filtered)


class IdentifierNormalizer(ast.NodeTransformer):
    def __init__(self):
        self.name_map = {}
        self.counter = 1

    def get_placeholder(self, original_name):
        if original_name in self.name_map:
            return self.name_map[original_name]

        new_name = f"VAR_{self.counter}"
        self.name_map[original_name] = new_name
        self.counter += 1
        return new_name

    def should_keep_name(self, name):
        if keyword.iskeyword(name):
            return True

        if name in {
            "True", "False", "None",
            "print", "len", "range", "enumerate",
            "sum", "min", "max", "sorted",
            "list", "dict", "set", "tuple",
            "str", "int", "float", "bool"
        }:
            return True

        return False

    def visit_FunctionDef(self, node):
        if not self.should_keep_name(node.name):
            node.name = self.get_placeholder(node.name)

        self.generic_visit(node)
        return node

    def visit_AsyncFunctionDef(self, node):
        if not self.should_keep_name(node.name):
            node.name = self.get_placeholder(node.name)

        self.generic_visit(node)
        return node

    def visit_ClassDef(self, node):
        if not self.should_keep_name(node.name):
            node.name = self.get_placeholder(node.name)

        self.generic_visit(node)
        return node

    def visit_Name(self, node):
        if not self.should_keep_name(node.id):
            node.id = self.get_placeholder(node.id)
        return node

    def visit_arg(self, node):
        if node.arg not in {"self", "cls"} and not self.should_keep_name(node.arg):
            node.arg = self.get_placeholder(node.arg)
        return node


def normalize_python_code(code):
    try:
        tree = ast.parse(code)
        normalizer = IdentifierNormalizer()
        normalized_tree = normalizer.visit(tree)
        ast.fix_missing_locations(normalized_tree)
        return ast.dump(normalized_tree, annotate_fields=False, include_attributes=False)
    except SyntaxError:
        return preprocess_raw_code(code)


def compute_pair_metrics(code_a, code_b):
    raw_a = preprocess_raw_code(code_a)
    raw_b = preprocess_raw_code(code_b)

    normalized_a = normalize_python_code(code_a)
    normalized_b = normalize_python_code(code_b)

    raw_similarity = text_similarity(raw_a, raw_b)
    normalized_similarity = text_similarity(normalized_a, normalized_b)

    return {
        "raw_similarity": raw_similarity,
        "normalized_similarity": normalized_similarity
    }


def build_analysis_results(upload_folder, file_names):
    results = []

    for file_name in file_names:
        path = f"{upload_folder}/{file_name}"
        code = read_file_content(path)

        best_match_name = None
        best_raw = 0.0
        best_normalized = 0.0
        best_score = -1.0

        for other_name in file_names:
            if other_name == file_name:
                continue

            other_path = f"{upload_folder}/{other_name}"
            other_code = read_file_content(other_path)

            metrics = compute_pair_metrics(code, other_code)

            combined_score = (
                metrics["raw_similarity"] * 0.40
                + metrics["normalized_similarity"] * 0.60
            )

            if combined_score > best_score:
                best_score = combined_score
                best_match_name = other_name
                best_raw = metrics["raw_similarity"]
                best_normalized = metrics["normalized_similarity"]

        if best_match_name is None:
            results.append({
                "file_name": file_name,
                "best_match_name": None,
                "raw_similarity": "-",
                "normalized_similarity": "-",
                "raw_similarity_value": None,
                "normalized_similarity_value": None,
                "ai_best_match_name": "Puudub",
                "ai_raw_similarity": "0%",
                "ai_normalized_similarity": "0%",
                "ai_raw_similarity_value": 0,
                "ai_normalized_similarity_value": 0,
                "material_similarity": "0%",
                "material_similarity_value": 0
            })
        else:
            results.append({
                "file_name": file_name,
                "best_match_name": best_match_name,
                "raw_similarity": safe_percentage(best_raw),
                "normalized_similarity": safe_percentage(best_normalized),
                "raw_similarity_value": round(best_raw * 100),
                "normalized_similarity_value": round(best_normalized * 100),
                "ai_best_match_name": "Puudub",
                "ai_raw_similarity": "0%",
                "ai_normalized_similarity": "0%",
                "ai_raw_similarity_value": 0,
                "ai_normalized_similarity_value": 0,
                "material_similarity": "0%",
                "material_similarity_value": 0
            })

    return results