# Cyber Attack Analyzer

## Description
Cyber Attack Analyzer is a simple cybersecurity project that extracts, stores, and analyses network attack data.  
It processes large CSV datasets, filters attack records, stores them in a SQLite database, and generates clean summary reports.

This project is ideal for learning and practicing basic cybersecurity data analysis.

---

## Project Structure

| File | Purpose |
|:-----|:--------|
| `csv_preview_tool.py` | Quickly preview the structure and sample rows of large CSV files. |
| `attack_analyzer.py` | Parse attack records from a CSV and store them into a local SQLite database (`attacks.db`). |
| `attack_summary.py` | Generate summary reports from the database: top attackers, top attack types, attack timeline, and most targeted ports. |

---

## How to Run

Make sure you are inside the project folder where the scripts are saved.

```bash
cd path/to/your/project-folder
```

Install pandas if needed:
```bash
pip install pandas
```

Run the scripts:

**Preview your CSV file (optional):**
```bash
python3 csv_preview_tool.py
```

**Extract attack data into a database:**
```bash
python3 attack_analyzer.py
```

**Analyse the stored attacks:**
```bash
python3 attack_summary.py
```

Note:
- `csv_preview_tool.py` and `attack_analyzer.py` will prompt you to enter the CSV filename.
- `attack_summary.py` will automatically analyse the existing `attacks.db` without asking for inputs.

---

## Requirements

- Python 3.x
- pandas
- sqlite3 (included with Python)

---

## Example CSV Input

The scripts expect CSV files with the following columns:
- `Source IP`
- `Destination IP`
- `Destination Port`
- `Timestamp`
- `Label`

---

## Example Dataset

This project was tested using a sample CSV file from the **CICIDS2017 dataset** (Canadian Institute for Cybersecurity).  
CICIDS2017 is a public dataset containing network traffic captures with a mixture of benign and malicious activities.

**Example file used:**  
[`Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv`](https://www.unb.ca/cic/datasets/ids-2017.html)

To access the full CICIDS2017 dataset, you must register and download it directly from the official source:  
[https://www.unb.ca/cic/datasets/ids-2017.html](https://www.unb.ca/cic/datasets/ids-2017.html)

---

## Author

Jorg Gradwohl

---

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing
Feel free to fork the repository if you'd like to explore or experiment with the project.
