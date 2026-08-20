import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient
from logger import logger

# =========================
# LOAD ENVIRONMENT
# =========================

load_dotenv()

hf_token = os.getenv("HF_TOKEN")


# =========================
# VALIDATE API TOKEN
# =========================

if not hf_token:
    logger.error("HF_TOKEN is missing from .env file")
    client = None
else:
    client = InferenceClient(
        provider="auto",
        api_key=hf_token
    )


# =========================
# MODEL
# =========================

MODEL = "meta-llama/Llama-3.1-8B-Instruct"


# =========================
# AI ANALYSIS FUNCTION
# =========================

def analyze_system(metrics, alerts, processes):

    if client is None:
        return (
            "AI analysis unavailable: "
            "Hugging Face API token is missing."
        )

    prompt = f"""
You are an AI system health monitoring assistant.

Analyze the following real-time computer system information.

CPU Usage: {metrics["cpu"]}%
Memory Usage: {metrics["memory"]}%
Disk Usage: {metrics["disk"]}%

System Alerts:
{alerts}

Top Resource-Consuming Processes:
{processes}

Provide a concise analysis containing:

1. Overall system condition
2. Most important issue
3. Severity: Low, Medium, High, or Critical
4. Possible cause
5. Recommended action

Use only the information provided.
Do not invent metrics or processes.
Keep the response practical and concise.
"""

    try:

        logger.info(
            "Starting AI system analysis"
        )

        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a system health "
                        "monitoring AI assistant."
                    )
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            max_tokens=500
        )

        result = response.choices[0].message.content

        logger.info(
            "AI system analysis completed successfully"
        )

        return result

    except Exception as e:

        logger.error(
            f"AI analysis failed: {str(e)}"
        )

        return (
            "AI analysis is currently unavailable. "
            "Please check the API configuration or try again later."
        )


# =========================
# TEST
# =========================

if __name__ == "__main__":

    test_metrics = {
        "cpu": 21.1,
        "memory": 89.3,
        "disk": 72.7
    }

    test_alerts = [
        "High memory usage detected"
    ]

    test_processes = [
        {
            "name": "Code.exe",
            "cpu": 0.0,
            "memory": 6.83
        },
        {
            "name": "msedgewebview2.exe",
            "cpu": 0.0,
            "memory": 6.58
        }
    ]

    result = analyze_system(
        test_metrics,
        test_alerts,
        test_processes
    )

    print("\n=== AI SYSTEM ANALYSIS ===")
    print(result)