# Cisco Network Backup Manager

A lightweight, Dockerized web application built with **Flask** and **Netmiko** to automate and manage configuration backups for Cisco network devices.

## Features

* **Web Interface:** Easily add, view, and manage multiple Cisco devices and credentials.
* **Isolated Directories:** Automatically organizes backups into individual folders based on the device's hostname.
* **Timestamped Backups:** Every backup file is stamped with the exact execution date and time (`YYYY-MM-DD_HH-MM-SS`) to prevent overwrites.
* **Space-Saving Compression:** Instantly compresses text configurations into `.zip` files to optimize disk space.
* **Dockerized Setup:** Fully containerized with persistent storage for configurations and database entries.

---

# Project Structure

```text
cisco_backup_app/
├── app.py                 # Flask Backend & Netmiko Automation logic
├── Dockerfile             # Docker image configuration
├── docker-compose.yml     # Docker Compose configuration
├── templates/
│   └── index.html         # Bootstrap-based web interface
└── network_backups/       # Automatically created (Stores zipped device backups)
```

---

# Getting Started (Docker Compose)

The fastest and easiest way to run the application is with **Docker Compose**.

## Prerequisites

Make sure you have the following installed:

* Docker Desktop
* Docker Compose

---

## Step 1: Clone the Repository

Clone this repository or copy the following files into a single project directory:

* `app.py`
* `Dockerfile`
* `docker-compose.yml`
* `templates/index.html`

---

## Step 2: Build and Start the Application

Run the following command from the project root:

```bash
docker-compose up -d --build
```

### Options

* `-d` → Runs the application in the background.
* `--build` → Rebuilds the Docker image before starting.

---

## Step 3: Open the Web Interface

After the container starts successfully, open your browser and visit:

```text
http://localhost:5000
```

---

# How to Use

### 1. Add Devices

Fill in the form with:

* Device Hostname
* Management IP Address
* Platform Type
* SSH Username
* SSH Password
* Enable Secret (optional)

### 2. Start Backup

Click:

> **Take Backup of All Devices**

The application will connect to every configured device via SSH and retrieve its running configuration.

### 3. Retrieve Backups

Backups are saved inside:

```text
network_backups/
```

Each device receives its own folder:

```text
network_backups/
├── Router1/
│   ├── Router1_2025-06-20_15-45-21.zip
│   └── Router1_2025-06-21_09-11-42.zip
├── Switch1/
│   └── Switch1_2025-06-20_15-45-28.zip
```

---

# Local Development (Without Docker)

If you prefer running the application directly with Python:

## Install Dependencies

```bash
pip install flask netmiko
```

---

## Modify `app.py`

At the bottom of `app.py`, ensure the following exists:

```python
if __name__ == '__main__':
    init_db()
    app.run(debug=True)
```

---

## Run the Application

```bash
python app.py
```

Open your browser:

```text
http://127.0.0.1:5000
```

---

# Security Best Practices

* **Protect Credentials**

  * Replace `app.secret_key` with a secure environment variable before deploying to production.

* **Network Connectivity**

  * Ensure the machine running the application has SSH (port 22) access to all target Cisco devices.

* **Credential Storage**

  * Avoid storing production credentials directly in source code.

---

# Technologies Used

* Python
* Flask
* Netmiko
* Docker
* Docker Compose
* Bootstrap
* SQLite

---

# License

This project is licensed under the **MIT License**.

Feel free to use, modify, and distribute it according to the terms of the license.
