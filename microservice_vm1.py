import os
import platform
import subprocess
from flask import Flask, render_template_string

app = Flask(__name__)

# Replace with actual IP addresses of your Virtual Machines
VM1_IP = "192.168.240.39"
VM2_IP = "192.168.240.40"

def is_vm_online(ip):
    """Ping the VM and check if it's online."""
    param = "-n" if platform.system().lower() == "windows" else "-c"
    try:
        output = subprocess.run(["ping", param, "1", ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return output.returncode == 0
    except Exception as e:
        print(f"Error pinging {ip}: {e}")
        return False

@app.route("/")
def index():
    """Check VM status and render the webpage."""
    vm1_status = "Online" if is_vm_online(VM1_IP) else "Offline"
    vm2_status = "Online" if is_vm_online(VM2_IP) else "Offline"
    system_name = platform.node()

    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>VM Ping Status</title>
        <style>
            body { font-family: Arial, sans-serif; text-align: center; }
            h1 { color: #007BFF; }
            .status { font-size: 18px; margin-top: 20px; }
            .online { color: green; }
            .offline { color: red; }
            iframe { width: 80%; height: 500px; margin-top: 20px; border: none; }
        </style>
    </head>
    <body>
        <h1>System: {{ system_name }}</h1>
        <p class="status">VM1 ({{ vm1_ip }}) Status: <span class="{{ vm1_class }}">{{ vm1_status }}</span></p>
        <p class="status">VM2 ({{ vm2_ip }}) Status: <span class="{{ vm2_class }}">{{ vm2_status }}</span></p>
        <iframe src="https://www.google.com" title="Google"></iframe>
    </body>
    </html>
    """

    return render_template_string(
        html_template,
        system_name=system_name,
        vm1_ip=VM1_IP,
        vm2_ip=VM2_IP,
        vm1_status=vm1_status,
        vm2_status=vm2_status,
        vm1_class="online" if vm1_status == "Online" else "offline",
        vm2_class="online" if vm2_status == "Online" else "offline"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
