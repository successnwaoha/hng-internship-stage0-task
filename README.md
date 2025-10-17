# HNG Internship Stage 0: Dynamic Profile API

## Project Overview

This project implements a simple RESTful API endpoint as part of the HNG Internship Stage 0 Backend task. The API returns dynamic profile information along with a random cat fact fetched from an external API (`https://catfact.ninja/fact`). This task demonstrates the ability to consume third-party APIs, format JSON responses, and manage dynamic data.

## Features

-   **`/me` Endpoint:** A GET endpoint that returns personal profile details.
-   **Dynamic Cat Facts:** Fetches a new, random cat fact on every request from the Cat Facts API.
-   **Dynamic Timestamp:** Provides the current UTC time in ISO 8601 format for each request.
-   **JSON Response:** Returns data in a strictly defined JSON format.
-   **Error Handling:** Gracefully handles failures when fetching data from the external Cat Facts API.

## Technologies Used

-   **Python 3:** The core programming language.
-   **Flask:** A lightweight web framework for building the API.
-   **Requests:** HTTP library for making API calls to `catfact.ninja`.
-   **python-dotenv:** For managing environment variables locally.
-   **Gunicorn:** A WSGI HTTP server used for production deployment.

## Project Structure

## Local Setup & Running

Follow these steps to set up and run the API on your local machine.

### 1. Clone the Repository

git clone https://github.com/successnwaoha/hng-internship-stage0-task
cd hng-internship-stage0-task

### 2. Create and Activate a Virtual Environment

Install all required Python packages using pip:
pip install -r requirements.txt

### 3. Install Dependencies

pip install -r requirements.txt

### 4. Configure Environment Variables

Create a file named .env in the root of your project directory (the same level as app.py). This file will hold your personal details. This file is excluded from Git tracking by .gitignore for security.

# .env
YOUR_EMAIL="your.email@example.com"      # Replace with your personal email
YOUR_NAME="Your Full Name"               # Replace with your full name
YOUR_STACK="Python/Flask"                # Replace with your backend stack

### 5. Run the Application

Start the Flask development server:

python app.py