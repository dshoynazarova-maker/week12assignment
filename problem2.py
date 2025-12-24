log_data = """[INFO] System started successfully
[WARNING] Memory usage high
[ERROR] Database connection failed
[INFO] User logged in
[ERROR] Payment gateway timeout
[INFO] Scheduled backup complete
[ERROR] Disk space critical"""

with open("server_log.txt", "w") as f:
    f.write(log_data)
with open("urgent_alerts.txt", "w") as file1 , open('server_log.txt', 'r') as file:
    counter = 0
    for line in file:
        if 'ERROR' in line:
            counter += 1
            file1.write(line)

    print(f'Scan complete. Found {counter} errors.')
    print(f'Please check urgent_alerts.txt.')
        


