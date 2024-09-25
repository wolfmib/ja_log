import os
from datetime import datetime

log_file = "/Users/johnny_hung/Documents/ja_interview_entretien/ja_git/ja_log/aws_log.txt"
log_file_clockify = "/Users/johnny_hung/Documents/ja_interview_entretien/ja_git/ja_log/clockify_log.txt"

# 10_000_000
def rotate_log(llog_file):
    if os.path.getsize(llog_file) > 10_000_000:  # Rotate if larger than 10MB
        # Rename the old log with a timestamp
        newfile = f"{llog_file}-{datetime.now().strftime('%Y-%m-%d-%H%M%S')}"
        os.rename(llog_file, newfile)

        # Start a new log file
        with open(llog_file, "w") as f:
            f.write(f"Log rotated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        print(f"Log rotated: {newfile}")

# Call the rotate_log function
if __name__ == "__main__":
    rotate_log(log_file)
    rotate_log(log_file_clockify)

