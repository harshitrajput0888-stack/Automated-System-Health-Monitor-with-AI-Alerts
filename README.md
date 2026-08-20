# Automated System Health Monitor with AI Alerts

An automated system monitoring application built with Python to monitor system resources, calculate system health, detect resource-related issues, generate alerts, analyze resource-consuming processes, and provide AI-powered recommendations.

## Features

- Real-time CPU usage monitoring
- Real-time memory usage monitoring
- Real-time disk usage monitoring
- Automatic system health score calculation
- Healthy, Warning, and Critical status classification
- System-level resource alerts
- Top resource-consuming process monitoring
- Process-level alerts
- Historical system metrics tracking
- CPU, memory, and disk usage charts
- AI-generated system analysis using Hugging Face
- AI-based recommendations for detected issues
- Application logging
- Automated testing with pytest
- Streamlit dashboard
- Cloud deployment

## Technology Stack

- Python 3.12
- psutil
- Pandas
- Matplotlib
- Streamlit
- Hugging Face Hub
- Hugging Face Inference API
- python-dotenv
- pytest
- CSV for historical metrics storage
- Git and GitHub
- Streamlit Community Cloud

## 🚀 Live Demo

[Automated-System-Health-Monitor-with-AI-Alerts](automated-system-health-monitor-with-ai-alerts∙main∙app/ui.py)

## Project Structure


Automated-System-Health-Monitor-with-AI-Alerts/
│
├── app/
│   ├── __init__.py
│   ├── ai_analyzer.py
│   ├── alerts.py
│   ├── charts.py
│   ├── config.py
│   ├── health.py
│   ├── history.py
│   ├── logger.py
│   ├── main.py
│   ├── monitor.py
│   ├── process_alerts.py
│   ├── process_monitor.py
│   └── ui.py
│
├── data/
│   ├── metrics.csv
│   ├── cpu_history.png
│   ├── memory_history.png
│   └── disk_history.png
│
├── tests/
│   ├── conftest.py
│   ├── test_alerts.py
│   ├── test_health.py
│   └── test_process_monitor.py
│
├── .gitignore
├── requirements.txt
└── README.md

## How It Works

1. The application collects real-time CPU, memory, and disk usage using `psutil`.
2. The collected metrics are processed by the health scoring module.
3. The system calculates an overall health score.
4. The system is classified as Healthy, Warning, or Critical.
5. Threshold-based rules detect high resource usage.
6. The process monitoring module identifies resource-consuming processes.
7. System and process-level alerts are generated.
8. System metrics are stored for historical analysis.
9. Historical CPU, memory, and disk usage are displayed through charts.
10. The Streamlit dashboard presents the complete monitoring information.
11. Relevant system information is sent to the Hugging Face AI service.
12. The AI generates system analysis and recommended actions.
13. Application activities and AI operations are recorded through logging.

## Health Status Classification

| Status | Health Score | Description |
|--------|--------------|-------------|
| Healthy | 80–100 | System resources are operating within acceptable limits |
| Warning | 60–79 | Resource usage requires attention |
| Critical | Below 60 | System resources indicate a potentially serious issue |

## Testing

The project uses pytest for automated testing.

Current test coverage includes:

- Health score calculation
- Health status classification
- CPU usage alerts
- Memory usage alerts
- Disk usage alerts
- Process monitoring
- Process data validation
- Process alert generation

Run the tests using:


pytest

## Configuration

The application uses environment-based configuration to securely manage the Hugging Face API token required for AI-powered system analysis.

Create a `.env` file in the project root:


HF_TOKEN=your_huggingface_token

## Running the Application

Activate the virtual environment on Windows:

.\venv\Scripts\Activate.ps1

Install the required dependencies:

pip install -r requirements.txt

Run the command-line monitoring engine:

python app/main.py

The monitoring engine displays CPU usage, memory usage, disk usage, health score, health status, top resource-consuming processes, and system alerts.

Run the Streamlit dashboard:

streamlit run app/ui.py

The Streamlit dashboard provides real-time system metrics, health status, process monitoring, system and process alerts, historical charts, AI-powered system analysis, and AI-generated recommendations.

The application is also deployed on Streamlit Community Cloud and can be accessed through the Live Demo link.

## Future Improvements

- Automatic periodic system monitoring and dashboard refresh
- Email and notification-based alerts for critical issues
- Advanced anomaly detection for unusual resource usage
- Database integration for long-term historical metrics
- Customizable CPU, memory, and disk alert thresholds
- Advanced AI-based root cause analysis
- Performance trend prediction using machine learning
- Server and cloud infrastructure monitoring
- Container and application-level monitoring
- Detailed performance reports and analytics

## Project Objective

The objective of this project is to develop an automated system health monitoring solution that continuously monitors CPU, memory, disk, and process usage, calculates overall system health, detects potential performance issues, generates alerts, and uses AI-powered analysis to provide understandable insights and recommended actions.

