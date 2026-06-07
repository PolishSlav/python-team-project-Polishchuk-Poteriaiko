def analyze_logs(logs):
    if not logs:
        return 0, [], []

    total_records = len(logs)

    errors = [log.strip() for log in logs if "[ERROR]" in log.upper()]
    warnings = [log.strip() for log in logs if "[WARNING]" in log.upper()]

    return total_records, errors, warnings


def generate_report(total, errors, warnings):
    report = "ANALYZER REPORT\n"
    report += f"Total records processed: {total}\n"
    report += f"Critical errors found (ERROR): {len(errors)}\n"
    report += f"Warnings found (WARNING): {len(warnings)}\n"

    if errors:
        report += "\nError Details\n"
        for err in errors:
            report += f" > {err}\n"

    if warnings:
        report += "\nWarnings Details\n"
        for war in warnings:
            report += f" > {war}\n"

    return report
