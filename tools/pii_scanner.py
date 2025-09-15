import re, sys, pathlib

PII_PATTERNS = {
    "email": re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"),
    "ssn": re.compile(r"\b\d{3}-\d{2}-\d{4}\b"),
    "phone": re.compile(
        r"\b(?:\+?\d{1,3})?[\s.-]?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}\b"
    ),
}


def scan_text(text: str):
    findings = []
    for name, pat in PII_PATTERNS.items():
        for m in pat.finditer(text):
            findings.append({"type": name, "match": m.group(0)})
    return findings


if __name__ == "__main__":
    path = pathlib.Path(sys.argv[1])
    txt = path.read_text(errors="ignore")
    fs = scan_text(txt)
    for f in fs:
        print(f)
    if fs:
        sys.exit(1)
