# 🏢 txt Registry Manager

A robust Python application built with **Tkinter** for managing, importing, and exporting company records. This tool is designed to serve as a bridge between different data formats, allowing users to seamlessly transition between legacy text systems, standard spreadsheets (CSV), and modern web-ready data (JSON).

## 🚀 Key Features
* **Multi-Format Support:** Import and export data in `.txt` (Pipe-delimited), `.csv`, and `.json`.
* **Dynamic UI:** Uses a `Treeview` table for real-time data visualization and editing.
* **Data Normalization:** Automatically maps inconsistent headers (e.g., "nombre" vs "name") to a standardized internal format.
* **Robust Type Casting:** Validates and converts currency/budget strings into float values for accurate data processing.

## 💻 Requirements
* **macOS / Linux / Windows**
* **Python 3.x**
* **Tkinter** (usually included with Python on Mac/Windows)

## 🛠 Installation & Setup
1. **Clone the repository:** `git clone https://github.com/JuanFe-Lozano-A/txt-registry-manager.git`
2. **Navigate to directory:** `cd txt-registry-manager`
3. **Create virtual environment:** `python3 -m venv .venv`
4. **Activate Environment (Mac/Linux):** `source .venv/bin/activate`
5. **Activate Environment (Windows):** `.venv\Scripts\activate`
6. **Install the application:** `pip install -e .`
7. **Launch the application:** `run-biz`
## 🚀 Quick Start

## 📖 Usage Guide
1. **Load Data:** Use the "Browse" button to select a file. The app will detect the extension and apply the correct parsing logic.
2. **Edit Records:** Modify data directly through the UI input fields.
3. **Save/Export:** Export your current session back to any of the three supported formats.

## 🧪 Testing Suite & Robustness Verification

This project includes a comprehensive testing suite located in the `/tests` directory. It covers three file formats (**TXT, CSV, JSON**) across two categories: **Standard Operations** and **Edge Case/Robustness** testing.

### 1. Standard "Happy Path" Tests
These files contain perfectly formatted data used to verify that the core import/export engine and the UI Treeview are functioning correctly.
* **Files:** `test_txt_1.txt`, `test_txt_2.txt`, `test_csv_1.csv`, `test_csv_2.csv`, `test_json_1.json`, `test_json_2.json`.
* **Expectation:** The data should load instantly, all columns should be populated, and no error messages should appear.
* **Goal:** Verify that basic read/write permissions and standard parsing logic are intact.

---