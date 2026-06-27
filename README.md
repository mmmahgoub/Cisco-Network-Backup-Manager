# Cisco Network Backup Manager

A lightweight, Dockerized web application built with **Flask** and **Netmiko** to automate and manage configuration backups for Cisco network devices. 

## Features
* **Web Interface:** Easily add, view, and manage multiple Cisco devices and credentials.
* **Isolated Directories:** Automatically organizes backups into individual folders based on the device's hostname.
* **Timestamped Backups:** Every backup file is stamped with the exact execution date and time (`YYYY-MM-DD_HH-MM-SS`) to prevent overwrites.
* **Space-Saving Compression:** Instantly compresses text configurations into `.zip` files to drastically optimize disk space.
* **Dockerized Setup:** Fully containerized with persistent storage for configurations and database entries.

---

## Project Structure
```text
cisco_backup_app/
├── app.py                 # Flask Backend & Netmiko Automation logic
├── Dockerfile             # Docker image configuration
├── docker-compose.yml     # Docker Compose multi-container management
├── templates/
│   └── index.html         # Front-end Web UI Bootstrap layout
└── network_backups/       # Created automatically (Stores your zipped device backups)

Getting Started (Using Docker Compose)
The fastest and most reliable way to run this application is using Docker and Docker Compose.

Prerequisites
Ensure you have the following installed on your machine:

Docker Desktop

Docker Compose

Step 1: Clone or Copy the Repository
Place all the project files (app.py, Dockerfile, docker-compose.yml, and templates/index.html) into a single directory on your host machine.

Step 2: Spin Up the Application
Open your terminal/command prompt in the root of the project directory and execute:

Bash
docker-compose up -d --build
The -d flag runs the container silently in the background, and --build ensures your latest configurations are applied.

Step 3: Access the Web Interface
Once the container status is healthy, open your preferred web browser and navigate to:

Plaintext
http://localhost:5000
How to Use
Add Your Devices: Use the form on the left pane to submit your device specifics (Hostname/Name, Management IP, Platform type, SSH Username, Password, and optional Enable Secret).

Trigger Backup: Click the "Take Backup of All Devices" button.

Retrieve Backups: Check the newly generated network_backups/ folder inside your host project directory. You will find separate directories for each device containing zipped backup configurations.

Local Development (Without Docker)
If you prefer to run the application natively on your Python environment, use the steps below:

Install Dependencies:

Bash
pip install flask netmiko
Modify app.py for local routing:
Change the bottom of app.py to allow local debugging:

Python
if __name__ == '__main__':
    init_db()
    app.run(debug=True)
Run the Script:

Bash
python app.py
Access via http://127.0.0.1:5000

Security Best Practices
Production Credentials: This tool handles sensitive infrastructure network credentials. In production environments, replace the app.secret_key in app.py with a robust environment variable.

Network Access: Ensure the host machine running this container has network/routing access (SSH port 22) to the target device IPs specified in the web UI.

License
This project is open-source and available under the MIT License.