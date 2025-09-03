import sys, datetime

TEMPLATE = open("templates/model_card_template.md").read()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python tools/model_card_generator.py <ModelName> > MODEL_CARD.md")
        sys.exit(2)
    name = sys.argv[1]
    out = TEMPLATE.replace("<Model Name>", name)
    stamp = datetime.date.today().isoformat()
    out = out.replace("**Date**:", f"**Date**: {stamp}")
    print(out)
