# Setup Instructions

How to get the RAI Toolkit running on your machine or in your organization.

## Quick Local Setup

If you just want to try the tools:

```bash
# Get the code
git clone https://github.com/oommensy/rai-toolkit.git
cd rai-toolkit

# Set up Python environment  
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install what you need
pip install -r requirements.txt

# Test it works
python tools/pii_scanner.py --help
```

## Docker Setup

If you want something more reproducible:

```bash
# Build the container
docker build -t rai-toolkit .

# Run it
docker run -it --rm -v $(pwd):/workspace rai-toolkit

# Or use docker-compose for a full setup
docker-compose up -d
```
```

### Option 2: Docker (Enterprise Ready)
```bash
# Build the container
docker build -t rai-toolkit .

# Run interactive session
docker run -it --rm -v $(pwd):/workspace rai-toolkit

# Run specific tools
docker run --rm -v $(pwd)/data:/data rai-toolkit python tools/pii_scanner.py --input /data/sample.txt
```

### Option 3: Docker Compose (Full Stack)
```bash
# Start all services
docker-compose up -d

# Access toolkit
docker-compose exec rai-toolkit bash

# View evaluation dashboard
open http://localhost:8080
```

## 📦 What Gets Installed

### Core Dependencies
- **Security:** `bandit`, `detect-secrets` - Code security scanning
- **Testing:** `pytest`, `pre-commit` - Quality assurance
- **AI/ML:** `numpy`, `transformers` - Model evaluation
- **Documentation:** `markdown-it-py` - Template processing

### Development Tools
- **Linting:** `flake8`, `black` - Code formatting
- **Type Checking:** `mypy` - Static analysis
- **Git Hooks:** `pre-commit` - Automated checks

## 🏢 Enterprise Deployment

### Production Environment
```bash
# Create production-ready environment
python3 -m venv /opt/rai-toolkit
source /opt/rai-toolkit/bin/activate
pip install --no-dev -r requirements.txt

# Set up as system service
sudo cp scripts/rai-toolkit.service /etc/systemd/system/
sudo systemctl enable rai-toolkit
sudo systemctl start rai-toolkit
```

### CI/CD Integration
```yaml
# Example GitHub Actions workflow
name: RAI Checks
on: [push, pull_request]
jobs:
  rai-validation:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Setup RAI Toolkit
        run: |
          pip install -r requirements.txt
          pre-commit install
      - name: Run RAI Checks
        run: |
          python tools/pii_scanner.py --input src/
          python tools/toxic_content_evaluator.py --input outputs/
```

## 🔧 Troubleshooting

### Common Issues

**Issue:** `ModuleNotFoundError: No module named 'transformers'`  
**Fix:** Ensure virtual environment is activated: `source rai-toolkit/bin/activate`

**Issue:** `Permission denied` when running tools  
**Fix:** Make scripts executable: `chmod +x tools/*.py`

**Issue:** Docker build fails  
**Fix:** Check Docker version: `docker --version` (requires 20.10+)

### Environment Validation
```bash
# Check Python version (requires 3.8+)
python --version

# Verify all dependencies
pip check

# Test core functionality
python -c "import tools.pii_scanner; print('✓ PII Scanner OK')"
python -c "import tools.toxic_content_evaluator; print('✓ Toxicity Evaluator OK')"
```

## 🛠️ Advanced Configuration

### Custom Installation
```bash
# Install only core tools (minimal setup)
pip install -r requirements-core.txt

# Install with GPU support
pip install -r requirements-gpu.txt

# Install development dependencies
pip install -r requirements-dev.txt
```

### Environment Variables
```bash
# Optional configuration
export RAI_CONFIG_PATH="/path/to/custom/config"
export RAI_LOG_LEVEL="INFO"
export RAI_CACHE_DIR="/tmp/rai-cache"
```

## 📊 Performance & Scaling

### Resource Requirements
- **Minimum:** 2GB RAM, 1 CPU core
- **Recommended:** 8GB RAM, 4 CPU cores
- **GPU Support:** CUDA 11.2+ for large model evaluation

### Scaling for Large Organizations
```yaml
# docker-compose.scale.yml
version: '3.8'
services:
  rai-workers:
    image: rai-toolkit:latest
    deploy:
      replicas: 4
    environment:
      - RAI_WORKER_MODE=true
  
  rai-dashboard:
    image: rai-toolkit:dashboard
    ports:
      - "8080:8080"
    depends_on:
      - rai-workers
```

## 📞 Support

- **Setup Issues:** Check this guide first, then open an issue
- **Enterprise Support:** Contact your DevOps team for Docker/K8s deployment
- **Custom Requirements:** Fork the repo and adapt `requirements.txt`

---

**💡 Next Steps:** After setup, check the [Quick Start Guide](QUICK_START.md) for role-based usage instructions!