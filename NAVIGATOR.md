# Find What You Need

Can't find the right tool or template? This page should help.

## What are you trying to do?

**Check something for problems:**
- Model outputs seem unsafe → `tools/toxic_content_evaluator.py`
- Dataset might be biased → `tools/dataset_bias_audit.py`  
- Code might have secrets → `tools/pii_scanner.py`
- Run full safety tests → `evals/runner.py`

**Document an AI system:**
- New model → `templates/model_card_template.md`
- New dataset → `templates/data_card_template.md`
- Project risks → `templates/risk_register_template.yaml`
- Privacy assessment → `templates/dpia_template.md`

**Set up governance:**
- Team AI policies → `policies/ai_use_policy.md`
- Incident response → `policies/incident_response_playbook.md`
- Model release process → `policies/model_release_policy.md`
- Data governance → `policies/data_governance_policy.md`

**Integrate with existing workflows:**
- CI/CD examples → `INTEGRATIONS.md`
- Code review process → `checklists/pr_rai_checklist.md`
- Deployment checklist → `checklists/deployment_rai_checklist.md`
- Environment setup → `SETUP.md`

**Just getting started:**
- New to this stuff → `QUICK_START.md`
- I'm a developer → `QUICK_START.md` (developer section)
- I handle compliance → `QUICK_START.md` (compliance section)
- I'm a manager → `QUICK_START.md` (leadership section)
│   ├─ Deployment process → checklists/deployment_rai_checklist.md
│   └─ Environment setup → SETUP.md
│
└─ I need HELP getting started
    ├─ I'm new to RAI → QUICK_START.md
    ├─ I'm a developer → QUICK_START.md#developers--devops
    ├─ I'm in compliance → QUICK_START.md#compliance--risk-officers
    └─ I'm leadership → QUICK_START.md#leadership--product-managers
```

## 🎯 Role-Based Quick Access

### 👩‍💻 **Data Scientists & ML Engineers**
**Top 3 Must-Haves:**
1. [Model Evaluation Suite](evals/runner.py) - Comprehensive model testing
2. [Bias Detection Tool](tools/dataset_bias_audit.py) - Dataset fairness analysis  
3. [Model Card Template](templates/model_card_template.md) - Documentation standard

**Quick Commands:**
```bash
# Evaluate model safety
python evals/runner.py --config evals/config.example.yaml

# Check dataset bias
python tools/dataset_bias_audit.py --dataset data.csv

# Generate model documentation
python tools/model_card_generator.py --model models/my_model
```

### 🛡️ **Compliance & Risk Officers**
**Top 3 Must-Haves:**
1. [Risk Register Template](templates/risk_register_template.yaml) - Project risk tracking
2. [AI Use Policy](policies/ai_use_policy.md) - Organizational guidelines
3. [Incident Response Playbook](policies/incident_response_playbook.md) - Crisis management

**Compliance Checklist:**
- [ ] AI use policy adopted and communicated
- [ ] Risk registers created for all AI projects
- [ ] Incident response procedures established
- [ ] Regular audit processes defined

### 👩‍💼 **Product & Engineering Managers**  
**Top 3 Must-Haves:**
1. [Integration Guide](INTEGRATIONS.md) - Workflow automation
2. [Deployment Checklist](checklists/deployment_rai_checklist.md) - Production readiness
3. [Quick Start Guide](QUICK_START.md) - Team onboarding

**Implementation Roadmap:**
1. **Week 1:** Team training with QUICK_START.md
2. **Week 2:** Integrate checklists into workflows  
3. **Week 3:** Set up automated checks (INTEGRATIONS.md)
4. **Week 4:** Establish governance policies

## 🔍 Resource Index by Use Case

### 🚨 **Emergency/Incident Response**
- **AI system causing harm:** → [Incident Response Playbook](policies/incident_response_playbook.md)
- **Data breach suspected:** → [PII Scanner](tools/pii_scanner.py) + playbook
- **Bias complaint received:** → [Bias Audit Tool](tools/dataset_bias_audit.py) + documentation
- **Toxic content detected:** → [Toxicity Evaluator](tools/toxic_content_evaluator.py) + mitigation steps

### 📋 **Planning & Setup**
- **New AI project:** → [Risk Register](templates/risk_register_template.yaml) + [AI Use Policy](policies/ai_use_policy.md)
- **Team onboarding:** → [Quick Start Guide](QUICK_START.md) + [Setup Instructions](SETUP.md)
- **Compliance audit prep:** → All templates + [Integration Examples](INTEGRATIONS.md)
- **Tool installation:** → [Setup Guide](SETUP.md) + Docker files

### 🔧 **Development & Testing**
- **Code review:** → [PR Checklist](checklists/pr_rai_checklist.md) + pre-commit hooks
- **Model validation:** → [Evaluation Suite](evals/) + [Safety Tools](tools/)
- **Documentation:** → [Template Index](templates/README.md) + examples
- **Deployment:** → [Deployment Checklist](checklists/deployment_rai_checklist.md)

### 📊 **Monitoring & Maintenance**
- **Production monitoring:** → [Integration Examples](INTEGRATIONS.md#model-monitoring-integration)
- **Regular audits:** → [Evaluation Tools](tools/) + [Risk Register Updates](templates/risk_register_template.yaml)
- **Policy updates:** → [Governance Documents](policies/) + version control
- **Team training:** → [Examples](examples/) + [Best Practices](QUICK_START.md#best-practices-for-organizations)

## 🛠️ Tool Selection Matrix

| Need | Beginner | Intermediate | Advanced | Enterprise |
|------|----------|--------------|----------|------------|
| **Toxicity Detection** | Manual review | `toxic_content_evaluator.py` | Automated CI/CD | Production monitoring |
| **Bias Detection** | Template audit | `dataset_bias_audit.py` | Pipeline integration | Real-time alerts |
| **PII Protection** | Manual checks | `pii_scanner.py` | Pre-commit hooks | GDPR compliance suite |
| **Documentation** | Basic templates | Generated cards | Automated updates | Audit-ready docs |
| **Governance** | Policy templates | Customized policies | Workflow integration | Enterprise compliance |

## 🚀 Getting Started Paths

### 🏃‍♀️ **Fast Track (30 minutes)**
1. Read [README.md](README.md) for overview
2. Follow [Quick Start](QUICK_START.md) for your role
3. Run one evaluation tool on sample data
4. Customize one template for your project

### 🚶‍♀️ **Comprehensive Setup (2 hours)**
1. Complete [Setup Guide](SETUP.md) with Docker
2. Configure [Integration](INTEGRATIONS.md) for your CI/CD
3. Establish [Governance Policies](policies/)
4. Train team with [Templates](templates/) and [Examples](examples/)

### 🏢 **Enterprise Rollout (1-2 weeks)**
1. **Week 1:** Leadership alignment + policy adoption
2. **Week 1:** Technical setup + integration
3. **Week 2:** Team training + workflow integration
4. **Week 2:** Monitoring setup + feedback loops

## 📞 Help & Support

### 🔗 **Quick Links**
- **Can't find something?** → Check this navigator first
- **Technical issues?** → [CONTRIBUTING.md](CONTRIBUTING.md) + GitHub issues
- **Policy questions?** → [Governance folder](policies/) + legal team
- **Integration help?** → [Integration examples](INTEGRATIONS.md) + DevOps team

### 📧 **Escalation Path**
1. **Self-service:** This navigator + documentation
2. **Community:** GitHub issues + discussions  
3. **Internal:** Your organization's AI/ML team
4. **Enterprise:** Vendor support (if applicable)

---

**💡 Pro Tip:** Bookmark this navigator and share it with your team - it's designed to be your central hub for all RAI Toolkit needs!