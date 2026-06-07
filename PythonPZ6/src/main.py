import sys
import os
from analyzer import analyze_logs, generate_report

def read_logs(filepath):
    if not os.path.exists(filepath):
        return []
    with open(filepath, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f.readlines() if line.strip()]

def main():
    filepath = "data/server.log"
    logs = read_logs(filepath)
    
    if not logs:
        print("Log file is empty or not found.")
        sys.exit(0)

    total, errors, warnings = analyze_logs(logs)
    report = generate_report(total, errors, warnings)
    
    print(report)
    
    with open("data/report.txt", "w", encoding="utf-8") as f:
        f.write(report)

if __name__ == "__main__":
    main()



