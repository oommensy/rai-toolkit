# Good First Issues for RAI Toolkit

Here are some beginner-friendly issues you can create on GitHub to help build your community:

## 🔍 **Issue 1: Add International PII Patterns**

**Title:** Add international phone number and ID formats to PII scanner

**Description:**
The current PII scanner only detects US formats. Help make it more globally useful!

**What needs to be done:**
- Add regex patterns for international phone numbers (UK, EU, etc.)
- Add patterns for international ID numbers (UK National Insurance, etc.) 
- Update the `PII_PATTERNS` dictionary in `tools/pii_scanner.py`
- Add test cases with international examples

**Good for:** First-time contributors, regex experience helpful but not required
**Estimated time:** 2-3 hours
**Files to modify:** `tools/pii_scanner.py`, `demo_data/`

---

## 📝 **Issue 2: Expand Toxicity Test Cases**

**Title:** Add more diverse toxicity prompts to evaluation suite

**Description:**
Help improve our toxicity detection by adding more test cases covering different types of harmful content.

**What needs to be done:**
- Add 20+ new toxicity prompts to `evals/cases/toxicity_prompts.jsonl`
- Include examples of: cyberbullying, hate speech, threats, harassment
- Ensure examples are diverse across different contexts
- Test that the evaluator properly flags them

**Good for:** Content moderation interest, understanding of harmful language patterns
**Estimated time:** 1-2 hours  
**Files to modify:** `evals/cases/toxicity_prompts.jsonl`

---

## 📊 **Issue 3: Create Example Model Cards**

**Title:** Write realistic model card examples for common AI use cases

**Description:**
Help teams understand how to document their models by creating more example model cards.

**What needs to be done:**
- Create 2-3 new model cards using the template
- Cover different domains: NLP, computer vision, recommendation systems
- Include realistic performance metrics, bias assessments, and limitations
- Follow the template in `templates/model_card_template.md`

**Good for:** ML practitioners, technical writing skills
**Estimated time:** 3-4 hours
**Files to modify:** `examples/` directory

---

## ♿ **Issue 4: Add Accessibility Checklist**

**Title:** Create accessibility checklist for AI system interfaces  

**Description:**
Ensure AI systems are accessible to users with disabilities by adding an accessibility review checklist.

**What needs to be done:**
- Research accessibility best practices for AI interfaces
- Create `checklists/accessibility_checklist.md`
- Include items for: screen readers, keyboard navigation, color contrast, etc.
- Add accessibility section to PR template

**Good for:** UX/accessibility advocates, research skills
**Estimated time:** 2-3 hours
**Files to create:** `checklists/accessibility_checklist.md`

---

## 🌍 **Issue 5: Add Multilingual Toxicity Detection**

**Title:** Extend toxicity evaluator to support non-English text

**Description:**
Make the toxicity evaluator work for global teams by adding multilingual support.

**What needs to be done:**
- Research multilingual toxicity detection libraries
- Add language detection to `tools/toxic_content_evaluator.py`
- Add test cases in Spanish, French, German, etc.
- Update documentation with multilingual examples

**Good for:** Multilingual developers, NLP interest
**Estimated time:** 4-5 hours
**Files to modify:** `tools/toxic_content_evaluator.py`, `evals/cases/`

---

## 📖 **Issue 6: Create Jupyter Notebook Tutorial**

**Title:** Build end-to-end tutorial showing all tools working together

**Description:**
Help new users understand the toolkit by creating an interactive tutorial.

**What needs to be done:**
- Create `tutorial.ipynb` in root directory
- Walk through: PII scanning → bias audit → toxicity check → documentation
- Use real (anonymized) dataset examples
- Include explanations of when to use each tool

**Good for:** Technical writers, Jupyter experience, educational content
**Estimated time:** 4-6 hours  
**Files to create:** `tutorial.ipynb`

---

To create these issues on GitHub:
1. Go to your repository → Issues → New issue
2. Copy the title and description from above
3. Add labels: `good first issue`, `help wanted`, `enhancement`
4. Add appropriate difficulty labels: `beginner`, `intermediate`