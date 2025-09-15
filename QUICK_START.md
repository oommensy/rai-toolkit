# Quick Start Guide: Find What You Need Fast

This guide helps you navigate the RAI Toolkit based on your role and needs. No more hunting through folders!

## 🎯 Choose Your Path

### 📊 Data Scientists & ML Engineers
**Goal:** Evaluate and improve model quality and safety

**Start Here:**
- `tools/toxic_content_evaluator.py` - Detect harmful content
- `tools/dataset_bias_audit.py` - Check for bias in datasets
- `evals/runner.py` - Run comprehensive model evaluations
- `templates/model_card_template.md` - Document your models

**Quick Commands:**
```bash
# Run toxicity evaluation
python tools/toxic_content_evaluator.py --input your_model_outputs.jsonl

# Check dataset bias
python tools/dataset_bias_audit.py --dataset your_data.csv

# Run full evaluation suite
python evals/runner.py --config evals/config.example.yaml
```

### 🛡️ Compliance & Risk Officers
**Goal:** Ensure governance, compliance, and risk management

**Start Here:**
- `policies/ai_use_policy.md` - Organization-wide AI guidelines
- `policies/incident_response_playbook.md` - Handle AI incidents
- `templates/risk_register_template.yaml` - Track and manage risks
- `templates/dpia_template.md` - Data protection impact assessments

**Action Items:**
1. Customize policies for your organization
2. Set up incident response procedures
3. Create risk registers for AI projects
4. Implement governance checklists

### 👩‍💻 Developers & DevOps
**Goal:** Integrate RAI into development workflows

**Start Here:**
- `checklists/pr_rai_checklist.md` - Pre-merge safety checks
- `checklists/deployment_rai_checklist.md` - Production readiness
- `.pre-commit-config.yaml` - Automated code quality checks
- `tools/pii_scanner.py` - Detect sensitive data

**Integration Steps:**
1. Install pre-commit hooks: `pre-commit install`
2. Add checklists to your PR templates
3. Integrate tools into CI/CD pipelines
4. Set up automated scanning

### 🏢 Leadership & Product Managers
**Goal:** Understand capabilities and business value

**Start Here:**
- `README.md` - Project overview and value proposition
- `ROADMAP.md` - Future capabilities and timeline
- `examples/` - Real-world usage examples
- `GOVERNANCE.md` - Project governance model

**Business Case:**
- Reduce compliance risk and audit preparation time
- Accelerate responsible AI adoption across teams
- Standardize quality and safety processes
- Demonstrate due diligence to stakeholders

## 🔍 Common Use Cases

### "I need to evaluate my model for safety issues"
→ Go to: `evals/` folder + `tools/toxic_content_evaluator.py`

### "I need to document my AI system for compliance"
→ Go to: `templates/model_card_template.md` + `templates/data_card_template.md`

### "I need to set up governance for our AI team"
→ Go to: `policies/` folder + `templates/risk_register_template.yaml`

### "I need to integrate safety checks into our workflow"
→ Go to: `checklists/` folder + `.pre-commit-config.yaml`

### "I found a bias or safety issue, now what?"
→ Go to: `policies/incident_response_playbook.md`

## 🚀 30-Second Setup

```bash
# Clone and setup
git clone <repo-url> && cd rai-toolkit
python3 -m venv rai-toolkit && source rai-toolkit/bin/activate
pip install -r requirements.txt

# Install development hooks
pre-commit install

# Test everything works
pytest -q
```

## 📞 Need Help?

- **Technical Issues:** Check `CONTRIBUTING.md` or open an issue
- **Policy Questions:** Review `policies/` folder or consult legal team
- **Integration Help:** See examples in each tool's documentation
- **Custom Requirements:** Fork the repo and adapt templates

---

**💡 Pro Tip:** Bookmark this page and share it with your team for quick reference!