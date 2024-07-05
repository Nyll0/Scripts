import psutil
import smtplib
from email.mime.text import MIMEText

# Define thresholds
CPU_THRESHOLD = 80.0
MEMORY_THRESHOLD = 80.0
DISK_THRESHOLD = 80.0

# Email settings
SMTP_SERVER = 'smtp.example.com'
SMTP_PORT = 587
EMAIL = 'your_email@example.com'
PASSWORD = 'your_password'
TO_EMAIL = 'recipient@example.com'

def send_alert(subject, message):
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = EMAIL
    msg['To'] = TO_EMAIL

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL, PASSWORD)
        server.sendmail(EMAIL, TO_EMAIL, msg.as_string())

def check_system_health():
    # Check CPU usage
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        send_alert('CPU Usage Alert', f'CPU usage is at {cpu_usage}%')

    # Check memory usage
    memory_info = psutil.virtual_memory()
    if memory_info.percent > MEMORY_THRESHOLD:
        send_alert('Memory Usage Alert', f'Memory usage is at {memory_info.percent}%')

    # Check disk usage
    disk_info = psutil.disk_usage('/')
    if disk_info.percent > DISK_THRESHOLD:
        send_alert('Disk Usage Alert', f'Disk usage is at {disk_info.percent}%')

if __name__ == '__main__':
    check_system_health()
