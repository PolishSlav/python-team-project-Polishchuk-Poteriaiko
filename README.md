# Log File Analyzer

A simple and efficient Python tool for analyzing server log files. It processes raw log data, counts total records, and extracts critical errors and warnings to generate a structured text report.

## 🛠 Features
* **Log Processing:** Reads `.log` files line by line.
* **Error Detection:** Automatically identifies and counts `[ERROR]` and `[WARNING]` entries.
* **Report Generation:** Creates a detailed summary report in `.txt` format.
* **Defensive Programming:** Safely handles empty files and missing directories.

## 📂 Project Structure
* `src/main.py` — The main script that handles file I/O operations.
* `src/analyzer.py` — The core logic module for parsing logs and generating the report.
* `Data/server.log` — Input directory and file for raw logs.
* `Data/report.txt` — Output file for the generated summary.

## 🚀 How to Run
1. Ensure you have Python 3 installed.
2. Place your raw log data in `Data/server.log`.
3. Navigate to the `src` folder and run the main script:
```bash
   python main.py