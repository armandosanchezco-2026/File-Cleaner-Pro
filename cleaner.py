import sys
from utils import (
    load_file,
    save_file,
    remove_empty_lines,
    remove_duplicates,
    normalize_spaces,
)

def clean_file(input_path, output_path):
    original = load_file(input_path)

    cleaned = normalize_spaces(original)
    cleaned = remove_empty_lines(cleaned)
    cleaned = remove_duplicates(cleaned)

    save_file(output_path, cleaned)

    print("\nFile cleaned successfully!")
    print(f"- Original lines: {len(original)}")
    print(f"- Clean lines: {len(cleaned)}")
    print(f"- Empty lines removed: {len(original) - len(remove_empty_lines(original))}")
    print(f"- Duplicates removed: {len(original) - len(remove_duplicates(original))}")
    print(f"- Output saved to: {output_path}\n")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("\nUsage:")
        print("  python cleaner.py input_file output_file\n")
        sys.exit(1)

    clean_file(sys.argv[1], sys.argv[2])
