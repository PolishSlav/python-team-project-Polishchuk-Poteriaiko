def analyze_logs(logs):
    total_records = len(logs)
    errors = [log for log in logs if "ERROR" in log]
    warnings = [log for log in logs if "WARNING" in log]
    return total_records, errors, warnings

def generate_report(total, errors, warnings):
    report = f"Total records: {total}\n"
    report += f"Errors found: {len(errors)}\n"
    report += f"Warnings found: {len(warnings)}\n"
    
    if errors:
        report += "\nErrors details:\n" + "\n".join(errors)
        
    return report



