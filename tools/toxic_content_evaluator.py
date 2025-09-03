import sys
BAD = {"hate", "kill", "idiot"}
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python tools/toxic_content_evaluator.py <file>")
        sys.exit(2)
    out = open(sys.argv[1]).read().lower().split()
    score = sum(t in BAD for t in out) / max(1, len(out))
    print({"toxicity_score": score})
    sys.exit(1 if score > 0.2 else 0)
