import os
import sys

ENTRY = "The fridge pushed a firmware update at 3am and bricked the ice maker. The apology notification arrived in English, Spanish, French, Japanese, and Developer."


def main() -> int:
    text = ENTRY.strip()
    n = len(text)
    print(f"LEN={n}")
    if not text or not (1 <= n <= 200):
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
