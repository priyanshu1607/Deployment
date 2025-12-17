# Deployment Bot

A Python-based automation tool designed to schedule deployments, send approval reminders via email, and trigger GitLab merge requests. This application uses FastAPI for the REST API and APScheduler for managing scheduled tasks.

## Features

- **Schedule Deployments**: Plan future deployments via a REST API.
- **Automated Reminders**: Sends email reminders for deployment approval prior to the scheduled time.
- **GitLab Integration**: Automatically triggers merge requests for specified target branches upon deployment execution.
- **Persistence**: Uses SQLite to persist deployment schedules and status.

## Prerequisites

- Python 3.7+
- A Gmail account (or other SMTP provider) for sending emails.
- GitLab account and project access (for Merge Request creation).

## Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd "deployment bot"
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requiremnt.txt
    ```
    *(Note: The requirements file is named `requiremnt.txt`)*

## Configuration

The application requires SMTP credentials to send emails. These are currently configured in `constants.py`.

1.  Open `constants.py`.
2.  Update the following variables with your credentials:
    ```python
    SMTP_HOST = "smtp.gmail.com"
    SMTP_PORT = 587
    SMTP_USER = "your-email@gmail.com"
    SMTP_PASS = "your-app-password"
    ```

## Usage

1.  **Start the server:**
    Run the application using `uvicorn` (or directly via python if configured, but `main.py` has a keep-alive loop):

    ```bash
    python main.py
    ```
    *Or if using uvicorn directly:*
    ```bash
    uvicorn main:app --reload
    ```

2.  **API Endpoints:**

    -   `POST /plan_deployment`: Schedule a new deployment.
        -   **Body:**
            ```json
            {
                "scheduled_time": "2024-12-25T10:00:00",
                "crm_record_id": "12345"
            }
            ```
    -   `GET /getJObs`: View currently recurring/scheduled jobs.
    -   `GET /DbQuerys`: (Debug) Clears database and returns all records.

## Project Structure

- `main.py`: Entry point for the FastAPI application.
- `scheduler.py`: Handles job scheduling and email logic.
- `database.py`: Database connection and session management.
- `models/`: Database models.
- `gitmanagement/`: GitLab integration logic.
