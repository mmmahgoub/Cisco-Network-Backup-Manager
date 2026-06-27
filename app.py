import os
import sqlite3
from datetime import datetime
import zipfile
from flask import Flask, render_template, request, redirect, url_for, flash
from netmiko import ConnectHandler

app = Flask(__name__)
app.secret_key = "super_secret_key_for_flash_messages"
DB_NAME = "devices.db"

# Initialize Database
def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS devices (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                ip TEXT NOT NULL,
                device_type TEXT NOT NULL,
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                secret TEXT
            )
        ''')
    conn.close()

# Helper to execute queries
def query_db(query, args=(), one=False):
    with sqlite3.connect(DB_NAME) as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute(query, args)
        rv = cur.fetchall()
        conn.commit()
    return (rv[0] if rv else None) if one else rv

@app.route('/')
def index():
    devices = query_db("SELECT * FROM devices")
    return render_template('index.html', devices=devices)

@app.route('/add_device', methods=['POST'])
def add_device():
    name = request.form['name']
    ip = request.form['ip']
    device_type = request.form['device_type']
    username = request.form['username']
    password = request.form['password']
    secret = request.form['secret']

    query_db(
        "INSERT INTO devices (name, ip, device_type, username, password, secret) VALUES (?, ?, ?, ?, ?, ?)",
        (name, ip, device_type, username, password, secret)
    )
    flash(f"Device '{name}' added successfully!", "success")
    return redirect(url_for('index'))

@app.route('/backup', methods=['POST'])
def run_backup():
    devices = query_db("SELECT * FROM devices")
    backup_root_path = request.form.get('backup_path', './backups').strip()
    
    if not devices:
        flash("No devices found to back up!", "danger")
        return redirect(url_for('index'))

    success_count = 0
    fail_count = 0
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    for device in devices:
        # Create device-specific folder inside the defined path
        device_folder = os.path.join(backup_root_path, device['name'])
        os.makedirs(device_folder, exist_ok=True)

        # File names
        txt_filename = f"{device['name']}_{timestamp}.txt"
        txt_filepath = os.path.join(device_folder, txt_filename)
        zip_filename = f"{device['name']}_{timestamp}.zip"
        zip_filepath = os.path.join(device_folder, zip_filename)

        try:
            # Establish SSH connection via Netmiko
            device_params = {
                'device_type': device['device_type'],
                'host': device['ip'],
                'username': device['username'],
                'password': device['password'],
                'secret': device['secret'] if device['secret'] else '',
            }
            
            net_connect = ConnectHandler(**device_params)
            
            # Enter enable mode if secret is provided
            if device['secret']:
                net_connect.enable()
                
            # Grab running configuration
            config = net_connect.send_command('show running-config')
            net_connect.disconnect()

            # Save configuration to a temporary text file
            with open(txt_filepath, 'w') as f:
                f.write(config)

            # Compress the text file into a .zip file
            with zipfile.ZipFile(zip_filepath, 'w', zipfile.ZIP_DEFLATED) as zipf:
                zipf.write(txt_filepath, arcname=txt_filename)

            # Clean up the raw text file to save space immediately
            os.remove(txt_filepath)
            success_count += 1

        except Exception as e:
            print(f"Error backing up {device['name']}: {str(e)}")
            fail_count += 1

    flash(f"Backup process finished! Success: {success_count}, Failed: {fail_count}. Saved to: {backup_root_path}", "info")
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)