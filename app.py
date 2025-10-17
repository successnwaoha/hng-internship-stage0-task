# app.py
from flask import Flask, jsonify
import requests
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# --- Configuration (from environment variables) ---
# It's good practice to get personal info from environment variables
# rather than hardcoding it directly in the code.
YOUR_EMAIL = os.getenv("YOUR_EMAIL", "your.email@example.com")
YOUR_NAME = os.getenv("YOUR_NAME", "Your Full Name")
YOUR_STACK = os.getenv("YOUR_STACK", "Python/Flask")

CAT_FACT_API_URL = "https://catfact.ninja/fact"
CAT_FACT_API_TIMEOUT = 5 # seconds

@app.route('/me', methods=['GET'])
def get_profile():
    # 1. Fetch a dynamic cat fact
    cat_fact = "Failed to fetch cat fact." # Fallback message
    try:
        response = requests.get(CAT_FACT_API_URL, timeout=CAT_FACT_API_TIMEOUT)
        response.raise_for_status() # Raise an exception for HTTP errors (4xx or 5xx)
        cat_fact_data = response.json()
        cat_fact = cat_fact_data.get("fact", cat_fact)
    except requests.exceptions.RequestException as e:
        app.logger.error(f"Error fetching cat fact: {e}")
        # You could also return an error response here if fact is critical
        # return jsonify({"status": "error", "message": "Could not retrieve cat fact"}), 500

    # 2. Get current UTC timestamp in ISO 8601 format
    current_utc_time = datetime.utcnow().isoformat() + "Z"

    # 3. Construct the response
    profile_data = {
        "status": "success",
        "user": {
            "email": YOUR_EMAIL,
            "name": YOUR_NAME,
            "stack": YOUR_STACK
        },
        "timestamp": current_utc_time,
        "fact": cat_fact
    }

    # 4. Return JSON response
    return jsonify(profile_data)

if __name__ == '__main__':
    # You can specify host and port if needed, e.g., host='0.0.0.0' for external access
    app.run()