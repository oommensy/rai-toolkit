# How to Integrate RAI Toolkit

Practical examples for adding responsible AI practices to your existing workflows.

## CI/CD Pipeline Integration

### GitHub Actions Workflow
```yaml
# .github/workflows/rai-checks.yml
name: Responsible AI Checks

on:
  pull_request:
    branches: [main, develop]
  push:
    branches: [main]

jobs:
  rai-validation:
    runs-on: ubuntu-latest
    name: RAI Safety Validation
    
    steps:
    - name: Checkout code
      uses: actions/checkout@v3
      
    - name: Setup Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'
        
    - name: Install RAI Toolkit
      run: |
        pip install -r requirements.txt
        pre-commit install
        
    - name: Run Security Scans
      run: |
        # Scan for PII in code and data
        python tools/pii_scanner.py --input src/ --output reports/pii_scan.json
        
        # Check for secrets and sensitive data
        detect-secrets scan --all-files --baseline .secrets.baseline
        
        # Security vulnerability scan
        bandit -r src/ -f json -o reports/security_scan.json
        
    - name: Evaluate Model Outputs
      if: contains(github.event.head_commit.message, '[model-update]')
      run: |
        # Test for toxic content
        python tools/toxic_content_evaluator.py \
          --input test_outputs/ \
          --threshold 0.1 \
          --output reports/toxicity_report.json
          
        # Run bias audit
        python tools/dataset_bias_audit.py \
          --dataset data/test_set.csv \
          --output reports/bias_audit.json
          
    - name: Validate Documentation
      run: |
        # Check model cards are up to date
        python tools/model_card_generator.py --validate --input models/
        
        # Ensure risk register is complete
        python scripts/validate_risk_register.py templates/risk_register.yaml
        
    - name: Upload Reports
      uses: actions/upload-artifact@v3
      with:
        name: rai-reports
        path: reports/
        
    - name: Comment PR Results
      if: github.event_name == 'pull_request'
      uses: actions/github-script@v6
      with:
        script: |
          const fs = require('fs');
          const reports = fs.readdirSync('reports/');
          let comment = '## 🛡️ RAI Toolkit Results\n\n';
          
          reports.forEach(report => {
            const content = fs.readFileSync(`reports/${report}`, 'utf8');
            comment += `### ${report}\n\`\`\`json\n${content}\n\`\`\`\n\n`;
          });
          
          github.rest.issues.createComment({
            issue_number: context.issue.number,
            owner: context.repo.owner,
            repo: context.repo.repo,
            body: comment
          });
```

### Jenkins Pipeline
```groovy
// Jenkinsfile
pipeline {
    agent any
    
    environment {
        RAI_REPORTS_DIR = 'rai-reports'
    }
    
    stages {
        stage('Setup RAI Toolkit') {
            steps {
                sh '''
                    python3 -m venv rai-env
                    source rai-env/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }
        
        stage('Pre-deployment RAI Checks') {
            parallel {
                stage('Security Scan') {
                    steps {
                        sh '''
                            source rai-env/bin/activate
                            mkdir -p ${RAI_REPORTS_DIR}
                            python tools/pii_scanner.py --input src/ --output ${RAI_REPORTS_DIR}/pii.json
                            detect-secrets scan --all-files --baseline .secrets.baseline
                        '''
                    }
                }
                
                stage('Model Evaluation') {
                    when {
                        anyOf {
                            changeset "models/**"
                            changeset "data/**"
                        }
                    }
                    steps {
                        sh '''
                            source rai-env/bin/activate
                            python evals/runner.py --config evals/production.yaml --output ${RAI_REPORTS_DIR}/eval.json
                        '''
                    }
                }
                
                stage('Documentation Check') {
                    steps {
                        sh '''
                            source rai-env/bin/activate
                            python tools/model_card_generator.py --validate --input models/
                        '''
                    }
                }
            }
        }
        
        stage('Generate RAI Report') {
            steps {
                script {
                    sh '''
                        source rai-env/bin/activate
                        python scripts/generate_deployment_report.py ${RAI_REPORTS_DIR}
                    '''
                    
                    publishHTML([
                        allowMissing: false,
                        alwaysLinkToLastBuild: true,
                        keepAll: true,
                        reportDir: RAI_REPORTS_DIR,
                        reportFiles: 'deployment_report.html',
                        reportName: 'RAI Deployment Report'
                    ])
                }
            }
        }
    }
    
    post {
        always {
            archiveArtifacts artifacts: 'rai-reports/**', fingerprint: true
        }
        failure {
            emailext (
                subject: "RAI Check Failed: ${env.JOB_NAME} - ${env.BUILD_NUMBER}",
                body: "RAI validation failed. Please check the reports before deployment.",
                to: "${env.CHANGE_AUTHOR_EMAIL}, ai-governance@company.com"
            )
        }
    }
}
```

## 🔄 Model Monitoring Integration

### Production Monitoring Script
```python
# scripts/production_monitor.py
import os
import json
import logging
from datetime import datetime
from tools.toxic_content_evaluator import ToxicContentEvaluator
from tools.dataset_bias_audit import BiasAuditor

class ProductionRAIMonitor:
    def __init__(self, config_path="config/monitor.yaml"):
        self.config = self.load_config(config_path)
        self.setup_logging()
        
    def monitor_model_outputs(self, model_id, outputs_path):
        """Monitor production model outputs for safety issues."""
        results = {
            'timestamp': datetime.now().isoformat(),
            'model_id': model_id,
            'checks': {}
        }
        
        # Toxicity check
        toxicity_evaluator = ToxicContentEvaluator()
        toxicity_results = toxicity_evaluator.evaluate_file(outputs_path)
        results['checks']['toxicity'] = toxicity_results
        
        # Bias check
        bias_auditor = BiasAuditor()
        bias_results = bias_auditor.audit_outputs(outputs_path)
        results['checks']['bias'] = bias_results
        
        # Alert if thresholds exceeded
        self.check_thresholds_and_alert(results)
        
        return results
    
    def check_thresholds_and_alert(self, results):
        """Send alerts if safety thresholds are exceeded."""
        toxicity_score = results['checks']['toxicity'].get('average_score', 0)
        bias_score = results['checks']['bias'].get('max_bias_score', 0)
        
        if toxicity_score > self.config['thresholds']['toxicity']:
            self.send_alert('TOXICITY_THRESHOLD_EXCEEDED', results)
            
        if bias_score > self.config['thresholds']['bias']:
            self.send_alert('BIAS_THRESHOLD_EXCEEDED', results)
    
    def send_alert(self, alert_type, results):
        """Send alert to monitoring system."""
        # Integration with Slack, PagerDuty, or internal systems
        pass

# Kubernetes CronJob for monitoring
# k8s/rai-monitor-cronjob.yaml
```

### Kubernetes Monitoring CronJob
```yaml
# k8s/rai-monitor-cronjob.yaml
apiVersion: batch/v1
kind: CronJob
metadata:
  name: rai-monitor
  namespace: ai-platform
spec:
  schedule: "0 */6 * * *"  # Every 6 hours
  jobTemplate:
    spec:
      template:
        spec:
          containers:
          - name: rai-monitor
            image: your-registry/rai-toolkit:latest
            command:
            - python
            - scripts/production_monitor.py
            env:
            - name: MODEL_OUTPUTS_PATH
              value: "/data/model-outputs"
            - name: ALERT_WEBHOOK
              valueFrom:
                secretKeyRef:
                  name: rai-config
                  key: alert-webhook
            volumeMounts:
            - name: model-outputs
              mountPath: /data/model-outputs
              readOnly: true
            - name: rai-config
              mountPath: /config
              readOnly: true
          volumes:
          - name: model-outputs
            persistentVolumeClaim:
              claimName: model-outputs-pvc
          - name: rai-config
            configMap:
              name: rai-monitor-config
          restartPolicy: OnFailure
```

## 📊 Data Pipeline Integration

### Apache Airflow DAG
```python
# dags/rai_data_pipeline.py
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'ai-team',
    'depends_on_past': False,
    'start_date': datetime(2025, 1, 1),
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def run_rai_checks(**context):
    """Run RAI checks on processed data."""
    import subprocess
    import json
    
    data_path = context['dag_run'].conf.get('data_path')
    
    # Run PII scan
    pii_result = subprocess.run([
        'python', 'tools/pii_scanner.py', 
        '--input', data_path,
        '--output', f'/tmp/pii_scan_{context["ts"]}.json'
    ], capture_output=True, text=True)
    
    # Run bias audit
    bias_result = subprocess.run([
        'python', 'tools/dataset_bias_audit.py',
        '--dataset', data_path,
        '--output', f'/tmp/bias_audit_{context["ts"]}.json'
    ], capture_output=True, text=True)
    
    # Check results and fail pipeline if issues found
    if pii_result.returncode != 0 or bias_result.returncode != 0:
        raise ValueError("RAI checks failed - pipeline stopped")

dag = DAG(
    'rai_data_pipeline',
    default_args=default_args,
    description='Data pipeline with RAI checks',
    schedule_interval=timedelta(days=1),
    catchup=False,
)

# Data processing task
process_data = BashOperator(
    task_id='process_data',
    bash_command='python scripts/process_data.py {{ dag_run.conf["data_path"] }}',
    dag=dag,
)

# RAI validation
rai_validation = PythonOperator(
    task_id='rai_validation',
    python_callable=run_rai_checks,
    dag=dag,
)

# Model training (only if RAI checks pass)
train_model = BashOperator(
    task_id='train_model',
    bash_command='python scripts/train_model.py {{ dag_run.conf["data_path"] }}',
    dag=dag,
)

process_data >> rai_validation >> train_model
```

## 🏢 Enterprise Integration Patterns

### Slack Integration for Alerts
```python
# integrations/slack_notifier.py
import json
import requests
from datetime import datetime

class SlackRAINotifier:
    def __init__(self, webhook_url):
        self.webhook_url = webhook_url
    
    def send_rai_alert(self, alert_type, details):
        """Send formatted RAI alert to Slack."""
        
        color_map = {
            'TOXICITY_THRESHOLD_EXCEEDED': 'danger',
            'BIAS_DETECTED': 'warning',  
            'PII_FOUND': 'danger',
            'DEPLOYMENT_BLOCKED': 'danger'
        }
        
        message = {
            "attachments": [{
                "color": color_map.get(alert_type, 'warning'),
                "title": f"🚨 RAI Alert: {alert_type}",
                "fields": [
                    {
                        "title": "Model/System",
                        "value": details.get('model_id', 'Unknown'),
                        "short": True
                    },
                    {
                        "title": "Timestamp", 
                        "value": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                        "short": True
                    },
                    {
                        "title": "Details",
                        "value": f"```{json.dumps(details, indent=2)}```",
                        "short": False
                    }
                ],
                "actions": [{
                    "type": "button",
                    "text": "View Full Report",
                    "url": details.get('report_url', '#')
                }]
            }]
        }
        
        response = requests.post(self.webhook_url, json=message)
        return response.status_code == 200
```

### JIRA Integration for Issue Tracking
```python
# integrations/jira_integration.py
from jira import JIRA

class RAIJiraIntegration:
    def __init__(self, server, username, api_token):
        self.jira = JIRA(server=server, basic_auth=(username, api_token))
    
    def create_rai_issue(self, issue_type, summary, description, priority='Medium'):
        """Create JIRA issue for RAI problems."""
        
        issue_dict = {
            'project': {'key': 'AI'},
            'summary': f"[RAI] {summary}",
            'description': description,
            'issuetype': {'name': 'Bug' if issue_type == 'violation' else 'Task'},
            'priority': {'name': priority},
            'labels': ['responsible-ai', 'compliance', issue_type],
            'components': [{'name': 'AI Safety'}]
        }
        
        issue = self.jira.create_issue(fields=issue_dict)
        return issue.key
```

## 📈 Metrics and Reporting

### Grafana Dashboard Configuration
```json
{
  "dashboard": {
    "title": "RAI Toolkit Metrics",
    "panels": [
      {
        "title": "Model Safety Scores",
        "type": "stat",
        "targets": [{
          "expr": "rai_toxicity_score",
          "legendFormat": "Toxicity Score"
        }],
        "thresholds": [
          {"color": "green", "value": 0},
          {"color": "yellow", "value": 0.1},
          {"color": "red", "value": 0.3}
        ]
      },
      {
        "title": "PII Detection Events",
        "type": "graph", 
        "targets": [{
          "expr": "rate(rai_pii_detections_total[5m])",
          "legendFormat": "PII Detections/min"
        }]
      },
      {
        "title": "Deployment Safety Gates",
        "type": "table",
        "targets": [{
          "expr": "rai_deployment_gate_status",
          "format": "table"
        }]
      }
    ]
  }
}
```

---

**💡 Next Steps:** 
1. Choose integration patterns that fit your tech stack
2. Customize thresholds and alerts for your risk tolerance  
3. Start with one integration and expand gradually
4. Train your teams on the new RAI workflows