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