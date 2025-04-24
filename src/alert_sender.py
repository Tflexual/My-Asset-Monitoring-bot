def send_alert(alerts):
    print(f"Alerts to send: {alerts}")  # Debugging print

    if alerts:
        for alert in alerts:
            print(f"ALERT: {alert}")
    else:
        print("No anomalies detected. No alerts sent.")  # Debugging print


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(alerts):
    sender_email = "oreoluwaodelola@gmail.com"
    receiver_email = "oluwatobiodelola25@gmail.com"
    password = "your_email_password"  # Use app-specific passwords for Gmail
    subject = "Asset Monitoring Alert"

    # Join all alerts into a single message
    body = "\n".join(alerts)

    # Create the email content
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Connect to Gmail SMTP server and send email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
        print("Email sent successfully.")
    except Exception as e:
        print(f"Error: {e}")


import csv
import os
from _datetime import datetime


def log_alerts_to_csv(alerts):
    log_file = "logs/alerts_log.csv"

    # Check if the file exists; if not, create it and add headers
    file_exists = os.path.isfile(log_file)

    with open(log_file, mode='a', newline='') as file:
        writer = csv.writer(file)

        # Write headers only if the file is being created
        if not file_exists:
            writer.writerow(["Timestamp", "Alert Message"])

        # Log each alert with a timestamp
        for alert in alerts:
            writer.writerow([datetime.now(), alert])

    print("Alerts logged to CSV.")



