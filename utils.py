import json

def remove_empty_lines(lines):
    return [line for line in lines if line.strip()]

def remove_duplicates(lines):
    seen = set()
    cleaned = []
    for line in lines:
        if line not in seen:
            cleaned.append(line)
            seen.add(line)
    return cleaned

def normalize_spaces(lines):
    return [" ".join(line.split()) + "\n" for line in lines]

def load_file(path):
    if path.endswith(".csv") or path.endswith(".txt"):
        with open(path, "r", encoding="utf-8") as f:
            return f.readlines()
    elif path.endswith(".json"):
        with open(path, "r", encoding="utf-8") as f:
            return json.dumps(json.load(f), indent=4).splitlines(True)
    else:
        raise ValueError("Unsupported file type")

def save_file(path, lines):
    with open(path, "w", encoding="utf-8") as f:
        f.writelines(lines)
