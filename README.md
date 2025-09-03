# Responsible AI Toolkit

Reusable code, policies, and checklists to help teams **build, evaluate, and ship AI systems responsibly**.

## Why
Organizations repeat RAI work (policies, checklists, basic scanners). This repo gives you **battle‑tested defaults** you can fork and tailor.

## Features
- **RAI CI**: pre‑commit + GitHub Actions for linting, secrets, dependency risk, and policy gates
- **Evaluations**: simple harness for jailbreak, toxicity, and hallucination prompts
- **Data hygiene**: PII and bias checks; datasheet + model card generators
- **Governance**: templates for policies, incident response, model release, and risk register

## Getting Started
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pre-commit install
pytest -q
```

## Contributing
See [CONTRIBUTING.md](CONTRIBUTING.md) and the [PR RAI Checklist](checklists/pr_rai_checklist.md).

## License
[MIT](LICENSE)
