def send_alert(message):
    print(f"[ALERT] {message}")
    with open("logs/intrusion_logs.txt", "a") as log_file:
        log_file.write(message + "\n")