from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

def create_deployment_bot_documentation():
    """Create comprehensive Deployment Bot documentation"""
    
    doc = Document()
    
    # Set default font
    style = doc.styles['Normal']
    font = style.font
    font.name = 'Calibri'
    font.size = Pt(11)
    
    # ========== TITLE PAGE ==========
    title = doc.add_heading('Deployment Bot Documentation', 0)
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    subtitle = doc.add_paragraph('Automated Deployment Scheduling and GitLab Integration')
    subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER
    subtitle.runs[0].font.size = Pt(14)
    subtitle.runs[0].font.color.rgb = RGBColor(100, 100, 100)
    
    doc.add_paragraph()
    version_para = doc.add_paragraph('Version 1.0')
    version_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    doc.add_page_break()
    
    # ========== TABLE OF CONTENTS ==========
    doc.add_heading('Table of Contents', 1)
    
    toc_items = [
        '1. Overview',
        '2. Features',
        '3. System Architecture',
        '4. Installation Guide',
        '5. Configuration',
        '6. API Reference',
        '7. Usage Examples',
        '8. Deployment Workflow',
        '9. Security Considerations',
        '10. Troubleshooting',
        '11. Production Deployment'
    ]
    
    for item in toc_items:
        doc.add_paragraph(item, style='List Number')
    
    doc.add_page_break()
    
    # ========== 1. OVERVIEW ==========
    doc.add_heading('1. Overview', 1)
    
    doc.add_paragraph(
        'The Deployment Bot is a Python-based automation system designed to streamline deployment '
        'processes by scheduling deployments, sending approval reminders via email, and automatically '
        'triggering GitLab merge requests with real-time pipeline monitoring.'
    )
    
    doc.add_paragraph(
        'This system is built using modern Python frameworks and follows best practices for '
        'asynchronous operations, making it efficient and scalable for CI/CD workflows.'
    )
    
    # Technology Stack Table
    doc.add_heading('Technology Stack', 2)
    
    table = doc.add_table(rows=7, cols=2)
    table.style = 'Light Grid Accent 1'
    
    tech_stack = [
        ('Component', 'Technology'),
        ('Web Framework', 'FastAPI'),
        ('ASGI Server', 'Uvicorn'),
        ('Task Scheduler', 'APScheduler'),
        ('Database', 'SQLite + SQLAlchemy ORM'),
        ('HTTP Client', 'httpx (async)'),
        ('Email', 'smtplib (SMTP)')
    ]
    
    for i, (component, tech) in enumerate(tech_stack):
        row = table.rows[i]
        row.cells[0].text = component
        row.cells[1].text = tech
        if i == 0:
            for cell in row.cells:
                for paragraph in cell.paragraphs:
                    for run in paragraph.runs:
                        run.font.bold = True
    
    doc.add_page_break()
    
    # ========== 2. FEATURES ==========
    doc.add_heading('2. Features', 1)
    
    doc.add_heading('Deployment Scheduling', 2)
    doc.add_paragraph('Schedule deployments for specific dates and times via REST API', style='List Bullet')
    doc.add_paragraph('Automatic job persistence across application restarts', style='List Bullet')
    doc.add_paragraph('Flexible scheduling with ISO 8601 datetime format', style='List Bullet')
    
    doc.add_heading('Automated Notifications', 2)
    doc.add_paragraph('Email reminders sent before deployment execution', style='List Bullet')
    doc.add_paragraph('Configurable reminder timing (default: 1 minute before deployment)', style='List Bullet')
    doc.add_paragraph('SMTP integration with Gmail and other providers', style='List Bullet')
    
    doc.add_heading('GitLab Integration', 2)
    doc.add_paragraph('Automatic Merge Request Creation for multiple target branches', style='List Bullet')
    doc.add_paragraph('Auto-Merge functionality upon MR creation', style='List Bullet')
    doc.add_paragraph('Real-time pipeline status monitoring', style='List Bullet')
    doc.add_paragraph('Parallel execution for processing multiple branches concurrently', style='List Bullet')
    doc.add_paragraph('Smart MR detection to reuse existing open MRs', style='List Bullet')
    
    doc.add_heading('Data Persistence', 2)
    doc.add_paragraph('SQLite database for deployment records', style='List Bullet')
    doc.add_paragraph('Track deployment status and approval state', style='List Bullet')
    doc.add_paragraph('Complete audit trail with creation and update timestamps', style='List Bullet')
    
    doc.add_heading('RESTful API', 2)
    doc.add_paragraph('FastAPI-powered endpoints', style='List Bullet')
    doc.add_paragraph('Automatic interactive documentation (Swagger UI)', style='List Bullet')
    doc.add_paragraph('JSON request/response format', style='List Bullet')
    
    doc.add_page_break()
    
    # ========== 3. SYSTEM ARCHITECTURE ==========
    doc.add_heading('3. System Architecture', 1)
    
    doc.add_paragraph(
        'The Deployment Bot follows a modular architecture with clear separation of concerns:'
    )
    
    doc.add_heading('Component Breakdown', 2)
    
    # API Layer
    doc.add_heading('API Layer (main.py)', 3)
    doc.add_paragraph(
        'Provides REST API endpoints for deployment management using FastAPI. '
        'Handles route definitions, database dependency injection, and application lifecycle.'
    )
    
    # Scheduling Layer
    doc.add_heading('Scheduling Layer (scheduler.py)', 3)
    doc.add_paragraph(
        'Manages job scheduling and execution using APScheduler. Handles both approval '
        'reminder jobs and deployment execution jobs with async support.'
    )
    
    # Data Layer
    doc.add_heading('Data Layer', 3)
    doc.add_paragraph(
        'Database configuration (database.py): SQLite database with SQLAlchemy ORM, '
        'thread-safe configuration for FastAPI compatibility.'
    )
    doc.add_paragraph(
        'Data Models (models/deployment.py): Deployment model with fields for scheduling, '
        'approval tracking, and status management.'
    )
    
    # Integration Layer
    doc.add_heading('Integration Layer (gitmanagement/gitlab.py)', 3)
    doc.add_paragraph(
        'Automates GitLab merge request creation and pipeline monitoring. Handles MR creation, '
        'auto-merge functionality, and real-time pipeline status polling.'
    )
    
    # Database Schema
    doc.add_heading('Database Schema', 2)
    
    schema_table = doc.add_table(rows=9, cols=3)
    schema_table.style = 'Light Grid Accent 1'
    
    schema_data = [
        ('Field', 'Type', 'Description'),
        ('id', 'Integer', 'Primary key (auto-increment)'),
        ('crm_record_id', 'String', 'External CRM reference'),
        ('scheduled_time', 'DateTime', 'When deployment should execute'),
        ('approval_reminder_time', 'DateTime', 'When to send approval reminder'),
        ('approval_status', 'String', 'pending, approved, rejected'),
        ('status', 'String', 'created, running, success, failed'),
        ('created_at', 'DateTime', 'Record creation timestamp'),
        ('updated_at', 'DateTime', 'Last update timestamp')
    ]
    
    for i, (field, type_val, desc) in enumerate(schema_data):
        row = schema_table.rows[i]
        row.cells[0].text = field
        row.cells[1].text = type_val
        row.cells[2].text = desc
        if i == 0:
            for cell in row.cells:
                for paragraph in cell.paragraphs:
                    for run in paragraph.runs:
                        run.font.bold = True
    
    doc.add_page_break()
    
    # ========== 4. INSTALLATION GUIDE ==========
    doc.add_heading('4. Installation Guide', 1)
    
    doc.add_heading('Prerequisites', 2)
    doc.add_paragraph('Python 3.7 or higher', style='List Bullet')
    doc.add_paragraph('Gmail account (for email notifications)', style='List Bullet')
    doc.add_paragraph('GitLab account with API access', style='List Bullet')
    
    doc.add_heading('Installation Steps', 2)
    
    p = doc.add_paragraph()
    p.add_run('Step 1: Clone the repository').bold = True
    doc.add_paragraph('git clone <repository-url>')
    doc.add_paragraph('cd "deployment bot"')
    
    p = doc.add_paragraph()
    p.add_run('Step 2: Install dependencies').bold = True
    doc.add_paragraph('pip install -r requirements.txt')
    
    p = doc.add_paragraph()
    p.add_run('Required packages:').bold = True
    doc.add_paragraph('fastapi==0.104.1', style='List Bullet')
    doc.add_paragraph('uvicorn[standard]==0.24.0', style='List Bullet')
    doc.add_paragraph('sqlalchemy==2.0.23', style='List Bullet')
    doc.add_paragraph('apscheduler==3.10.4', style='List Bullet')
    doc.add_paragraph('httpx==0.25.2', style='List Bullet')
    doc.add_paragraph('python-multipart==0.0.6', style='List Bullet')
    
    p = doc.add_paragraph()
    p.add_run('Step 3: Run the application').bold = True
    doc.add_paragraph('uvicorn main:app --reload')
    
    p = doc.add_paragraph()
    p.add_run('Step 4: Access the API').bold = True
    doc.add_paragraph('API: http://localhost:8000', style='List Bullet')
    doc.add_paragraph('Interactive Docs: http://localhost:8000/docs', style='List Bullet')
    
    doc.add_page_break()
    
    # ========== 5. CONFIGURATION ==========
    doc.add_heading('5. Configuration', 1)
    
    doc.add_heading('SMTP Configuration (constants.py)', 2)
    doc.add_paragraph('Configure email settings for sending approval reminders:')
    doc.add_paragraph('SMTP_HOST = "smtp.gmail.com"')
    doc.add_paragraph('SMTP_PORT = 587')
    doc.add_paragraph('SMTP_USER = "your-email@gmail.com"')
    doc.add_paragraph('SMTP_PASS = "your-app-password"  # Gmail App Password')
    
    p = doc.add_paragraph()
    p.add_run('WARNING: Never commit real credentials to version control. Use environment variables in production.').bold = True
    
    doc.add_heading('GitLab Configuration (gitmanagement/gitlab.py)', 2)
    
    p = doc.add_paragraph()
    p.add_run('Line 7: Set your GitLab token').bold = True
    doc.add_paragraph('headers = { "PRIVATE-TOKEN": "your-gitlab-token" }')
    
    p = doc.add_paragraph()
    p.add_run('Line 24: Set your project ID').bold = True
    doc.add_paragraph('Project_id = 74904249  # Replace with your project ID')
    
    p = doc.add_paragraph()
    p.add_run('Line 95: Configure target branches').bold = True
    doc.add_paragraph("TargetBranches = ['production', 'staging', 'development']")
    
    p = doc.add_paragraph()
    p.add_run('Finding your GitLab Project ID:').bold = True
    doc.add_paragraph('Navigate to your GitLab project', style='List Bullet')
    doc.add_paragraph('Look under the project name', style='List Bullet')
    doc.add_paragraph('You will see "Project ID: 12345678"', style='List Bullet')
    
    doc.add_page_break()
    
    # ========== 6. API REFERENCE ==========
    doc.add_heading('6. API Reference', 1)
    
    doc.add_heading('POST /plan_deployment', 2)
    doc.add_paragraph('Schedule a new deployment with automatic approval reminder and GitLab MR execution.')
    
    p = doc.add_paragraph()
    p.add_run('Request Body:').bold = True
    doc.add_paragraph('{')
    doc.add_paragraph('  "scheduled_time": "2024-12-25T10:00:00",')
    doc.add_paragraph('  "crm_record_id": "CRM-12345"')
    doc.add_paragraph('}')
    
    p = doc.add_paragraph()
    p.add_run('Response:').bold = True
    doc.add_paragraph('{')
    doc.add_paragraph('  "item_received": {')
    doc.add_paragraph('    "id": 1,')
    doc.add_paragraph('    "crm_record_id": "CRM-12345",')
    doc.add_paragraph('    "scheduled_time": "2024-12-25T10:00:00",')
    doc.add_paragraph('    "approval_reminder_time": "2024-12-25T09:59:00",')
    doc.add_paragraph('    "approval_status": "pending",')
    doc.add_paragraph('    "status": "created"')
    doc.add_paragraph('  }')
    doc.add_paragraph('}')
    
    doc.add_heading('GET /getJObs', 2)
    doc.add_paragraph('Retrieve all currently scheduled jobs in the scheduler.')
    doc.add_paragraph('Returns "exsist" if jobs are scheduled, 0 if no jobs.')
    
    doc.add_heading('GET /DbQuerys', 2)
    doc.add_paragraph('DEBUG ENDPOINT ONLY - Deletes all deployment records and returns empty array.')
    
    doc.add_page_break()
    
    # ========== 7. USAGE EXAMPLES ==========
    doc.add_heading('7. Usage Examples', 1)
    
    doc.add_heading('cURL Example', 2)
    doc.add_paragraph('curl -X POST http://localhost:8000/plan_deployment \\')
    doc.add_paragraph('  -H "Content-Type: application/json" \\')
    doc.add_paragraph("  -d '{")
    doc.add_paragraph('    "scheduled_time": "2024-12-25T10:00:00",')
    doc.add_paragraph('    "crm_record_id": "CRM-12345"')
    doc.add_paragraph("  }'")
    
    doc.add_heading('Python Example', 2)
    doc.add_paragraph('import requests')
    doc.add_paragraph('from datetime import datetime, timedelta')
    doc.add_paragraph('')
    doc.add_paragraph('deployment_time = datetime.now() + timedelta(days=1)')
    doc.add_paragraph('deployment_time = deployment_time.replace(hour=10, minute=0)')
    doc.add_paragraph('')
    doc.add_paragraph('response = requests.post(')
    doc.add_paragraph('    "http://localhost:8000/plan_deployment",')
    doc.add_paragraph('    json={')
    doc.add_paragraph('        "scheduled_time": deployment_time.isoformat(),')
    doc.add_paragraph('        "crm_record_id": "CRM-12345"')
    doc.add_paragraph('    }')
    doc.add_paragraph(')')
    doc.add_paragraph('print(response.json())')
    
    doc.add_page_break()
    
    # ========== 8. DEPLOYMENT WORKFLOW ==========
    doc.add_heading('8. Deployment Workflow', 1)
    
    doc.add_paragraph('The deployment process follows these steps:')
    
    p = doc.add_paragraph()
    p.add_run('1. Schedule Deployment').bold = True
    doc.add_paragraph('User sends POST request to /plan_deployment', style='List Bullet')
    doc.add_paragraph('System creates database record with status "created"', style='List Bullet')
    doc.add_paragraph('Schedules approval reminder job', style='List Bullet')
    doc.add_paragraph('Schedules deployment execution job', style='List Bullet')
    
    p = doc.add_paragraph()
    p.add_run('2. Approval Reminder').bold = True
    doc.add_paragraph('At reminder time (default: 1 minute before deployment)', style='List Bullet')
    doc.add_paragraph('System sends email notification', style='List Bullet')
    doc.add_paragraph('Logs reminder sent successfully', style='List Bullet')
    
    p = doc.add_paragraph()
    p.add_run('3. Deployment Execution').bold = True
    doc.add_paragraph('At scheduled deployment time', style='List Bullet')
    doc.add_paragraph('Creates merge requests for all target branches in parallel', style='List Bullet')
    doc.add_paragraph('Automatically merges each MR', style='List Bullet')
    doc.add_paragraph('Monitors pipeline status for each branch', style='List Bullet')
    doc.add_paragraph('Returns overall status (success or failed)', style='List Bullet')
    
    p = doc.add_paragraph()
    p.add_run('4. GitLab Integration Details').bold = True
    doc.add_paragraph('Source Branch: testingbranch (configurable)', style='List Bullet')
    doc.add_paragraph('Target Branches: push_from, Pipleine3, Pipleine2 (configurable)', style='List Bullet')
    doc.add_paragraph('Checks for existing open MRs before creating new ones', style='List Bullet')
    doc.add_paragraph('Polls pipeline status every 1 second until completion', style='List Bullet')
    
    doc.add_page_break()
    
    # ========== 9. SECURITY CONSIDERATIONS ==========
    doc.add_heading('9. Security Considerations', 1)
    
    p = doc.add_paragraph()
    p.add_run('CAUTION: This application is currently configured for development use only.').bold = True
    
    doc.add_heading('Current Security Issues', 2)
    doc.add_paragraph('Exposed Credentials: SMTP and GitLab credentials in source code', style='List Bullet')
    doc.add_paragraph('No Authentication: API endpoints are publicly accessible', style='List Bullet')
    doc.add_paragraph('No Input Validation: Limited validation on incoming requests', style='List Bullet')
    doc.add_paragraph('No Rate Limiting: API can be abused', style='List Bullet')
    
    doc.add_heading('Recommended Security Enhancements', 2)
    doc.add_paragraph('Move credentials to environment variables or secret management system', style='List Bullet')
    doc.add_paragraph('Implement API authentication (JWT, API keys, etc.)', style='List Bullet')
    doc.add_paragraph('Add input validation using Pydantic models', style='List Bullet')
    doc.add_paragraph('Implement rate limiting', style='List Bullet')
    doc.add_paragraph('Use HTTPS in production', style='List Bullet')
    doc.add_paragraph('Rotate GitLab tokens regularly', style='List Bullet')
    doc.add_paragraph('Set up proper logging and monitoring', style='List Bullet')
    doc.add_paragraph('Use a production-grade database (PostgreSQL)', style='List Bullet')
    
    doc.add_page_break()
    
    # ========== 10. TROUBLESHOOTING ==========
    doc.add_heading('10. Troubleshooting', 1)
    
    doc.add_heading('Common Issues and Solutions', 2)
    
    p = doc.add_paragraph()
    p.add_run('Issue: "Module not found" errors').bold = True
    doc.add_paragraph('Solution: Ensure all dependencies are installed')
    doc.add_paragraph('pip install -r requirements.txt')
    
    p = doc.add_paragraph()
    p.add_run('Issue: "Address already in use"').bold = True
    doc.add_paragraph('Solution: Another process is using port 8000')
    doc.add_paragraph('uvicorn main:app --port 8001')
    doc.add_paragraph('# Or kill the process using port 8000')
    
    p = doc.add_paragraph()
    p.add_run('Issue: Email not sending').bold = True
    doc.add_paragraph('Possible causes:')
    doc.add_paragraph('Incorrect SMTP credentials', style='List Bullet')
    doc.add_paragraph('App Password not generated', style='List Bullet')
    doc.add_paragraph('2-Step Verification not enabled', style='List Bullet')
    doc.add_paragraph('Email code still commented out', style='List Bullet')
    
    p = doc.add_paragraph()
    p.add_run('Issue: GitLab API errors').bold = True
    doc.add_paragraph('Possible causes:')
    doc.add_paragraph('Invalid access token', style='List Bullet')
    doc.add_paragraph('Insufficient permissions', style='List Bullet')
    doc.add_paragraph('Incorrect project ID', style='List Bullet')
    doc.add_paragraph("Branches don't exist", style='List Bullet')
    
    doc.add_page_break()
    
    # ========== 11. PRODUCTION DEPLOYMENT ==========
    doc.add_heading('11. Production Deployment', 1)
    
    doc.add_heading('Production Checklist', 2)
    
    checklist_items = [
        'Move credentials to environment variables',
        'Implement API authentication (JWT, API keys)',
        'Enable HTTPS/TLS',
        'Add input validation and sanitization',
        'Implement rate limiting',
        'Set up proper logging and monitoring',
        'Use a production-grade database (PostgreSQL)',
        'Rotate GitLab tokens regularly',
        'Configure a process manager (systemd, supervisor)',
        'Set up a reverse proxy (nginx)',
        'Implement automated backups',
        'Configure log rotation'
    ]
    
    for item in checklist_items:
        doc.add_paragraph(item, style='List Bullet')
    
    doc.add_heading('Environment Variables', 2)
    doc.add_paragraph('Create a .env file with the following variables:')
    doc.add_paragraph('SMTP_HOST=smtp.gmail.com')
    doc.add_paragraph('SMTP_PORT=587')
    doc.add_paragraph('SMTP_USER=your-email@gmail.com')
    doc.add_paragraph('SMTP_PASS=your-app-password')
    doc.add_paragraph('GITLAB_TOKEN=your-gitlab-token')
    doc.add_paragraph('GITLAB_PROJECT_ID=12345678')
    doc.add_paragraph('DATABASE_URL=postgresql://user:pass@localhost/deployments')
    
    doc.add_heading('Docker Deployment', 2)
    doc.add_paragraph('Example Dockerfile:')
    doc.add_paragraph('FROM python:3.11-slim')
    doc.add_paragraph('WORKDIR /app')
    doc.add_paragraph('COPY requirements.txt .')
    doc.add_paragraph('RUN pip install -r requirements.txt')
    doc.add_paragraph('COPY . .')
    doc.add_paragraph('CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]')
    
    # ========== FOOTER ==========
    doc.add_page_break()
    footer_para = doc.add_paragraph('End of Documentation')
    footer_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    footer_para.runs[0].font.color.rgb = RGBColor(150, 150, 150)
    
    # Save the document
    doc.save('Deployment_Bot_Documentation.docx')
    print("\n✅ Documentation created successfully: Deployment_Bot_Documentation.docx")

if __name__ == '__main__':
    create_deployment_bot_documentation()
