# Automated System Health Monitor with AI Alerts
🚀 [Live Demo](https://automated-system-health-monitor-with-ai-alerts.streamlit.app/)

An AI-assisted system monitoring application built with Python that tracks system resources, monitors running processes, detects abnormal resource usage, stores historical metrics, and generates AI-powered recommendations.

## Features

- Real-time CPU usage monitoring
- Real-time memory usage monitoring
- Disk usage monitoring
- Overall system health score
- Health status classification
- Automatic system alerts
- Top resource-consuming process monitoring
- Process-level alerts
- Historical CPU, memory, and disk tracking
- Historical metric charts
- Streamlit monitoring dashboard
- AI-powered system analysis
- AI-generated recommendations using Hugging Face
- Application logging
- API error handling
- Automated testing with pytest

## Technologies Used

- Python
- Streamlit
- psutil
- Pandas
- Matplotlib
- Hugging Face API
- python-dotenv
- Pytest

## Project Architecture

```text
System
   |
   v
System Metrics
   |
   +----> Health Scoring
   |
   +----> Alert Engine
   |
   +----> Process Monitoring
   |
   +----> Historical Data
   |
   v
Streamlit Dashboard
   |
   v
Hugging Face AI Analysis
   |
   v
Recommendations