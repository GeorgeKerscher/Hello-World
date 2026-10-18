from pathlib import Path
import re
import sys

# Mapping of ASCII fractions to Unicode fractions
FRACTION_MAP = {
    "1/4": "¼",
    "3/4": "¾",
    "2/3": "⅔",
    "1/2": "½",
}

def convert_fractions(text: str) -> str:
    """Replace supported ASCII fractions with Unicode equivalents."""

    # Sort by length to avoid partial matches
    pattern = re.compile(
        r'(?<!\d)(' + '|'.join(re.escape(k) for k in sorted(FRACTION_MAP, key=len, reverse=True)) + r')(?!\d)'
    )

    return pattern.sub(lambda m: FRACTION_MAP[m.group(0)], text)

def process_file(filename: str):
    input_path = Path(filename)

    if not input_path.exists():
        raise FileNotFoundError(f"File not found: {filename}")

    if input_path.suffix.lower() not in {".txt", ".md"}:
        raise ValueError("Only .txt and .md files are supported.")

    text = input_path.read_text(encoding="utf-8")

    updated_text = convert_fractions(text)

    output_path = input_path.with_name(
        f"{input_path.stem}_updated{input_path.suffix}"
    )

    output_path.write_text(updated_text, encoding="utf-8")

    print(f"Saved updated file: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python {Path(sys.argv[0]).name} <filename>")
        sys.exit(1)

    process_file(sys.argv[1])