import sys

SUSPICIOUS = [
    "ignore previous",
    "developer mode",
    "exfiltrate",
    "\n\n\n",
    "system prompt",
]

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python tools/prompt_injection_scanner.py <file>")
        sys.exit(2)
    text = open(sys.argv[1]).read().lower()
    hits = [w for w in SUSPICIOUS if w in text]
    print({"hits": hits})
    sys.exit(1 if hits else 0)
