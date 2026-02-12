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

### 2. Robustness & Error-Prone Tests
These tests deliberately challenge the program's logic to ensure it doesn't crash when encountering "dirty" or unexpected data.

#### **Text File (`.txt`) Edge Cases**
| Test File | Logic Targeted | Expected Outcome |
| :--- | :--- | :--- |
| `test_txt_missing_cols` | `IndexError` prevention. | App skips lines with fewer than 4 parts or shows a warning. |
| `test_txt_extra_pipes` | Delimiter splitting. | App prioritizes the first 4 columns or handles extra pipes gracefully. |
| `test_txt_empty_lines` | Iterator robustness. | The `for line in f` loop ignores blank lines without crashing. |
| `test_txt_bad_budget` | Type casting (`float`). | Triggers a `ValueError` handled by a message box, preventing a crash. |
| `test_txt_encoding` | UTF-8 Character Map. | Accents (á, é) and special characters (ñ) display correctly in the Treeview. |

#### **CSV File Edge Cases**
| Test File | Logic Targeted | Expected Outcome |
| :--- | :--- | :--- |
| `test_csv_spanish_headers`| Key Mapping logic. | Successfully maps `nombre` to `name` using the `.get()` fallback. |
| `test_csv_missing_headers` | Header mismatch. | App provides empty strings for missing keys instead of crashing. |
| `test_csv_quoted_commas` | Complex Parsing. | Names like "Company, Inc." remain one column, not split into two. |
| `test_csv_trailing_commas` | Column overflow. | Extra empty columns at the end of rows are ignored. |
| `test_csv_scientific_notation`| Float conversion. | Numbers like `1e5` are correctly converted to `100000.0`. |

#### **JSON File Edge Cases**
| Test File | Logic Targeted | Expected Outcome |
| :--- | :--- | :--- |
| `test_json_missing_keys` | Dictionary `.get()` safety. | Missing fields in an object default to `""` or `0`. |
| `test_json_wrong_types` | Data Integrity. | If a budget is an `Array` or `Boolean`, the app handles the type error gracefully. |
| `test_json_corrupted` | Syntax validation. | A `json.JSONDecodeError` is caught and reported via the UI. |
| `test_json_nulls` | `NoneType` handling. | `null` values in JSON are converted to empty strings for the UI. |
| `test_json_empty_array` | Zero-state handling. | Loading `[]` clears the Treeview without error. |

---

### 🛠 How to Run Tests

1. **Launch the Application:**

2. **Importing:**
   * Click the **"Browse"** button in the File Path section.
   * Navigate to the `tests/` folder.
   * Select any of the files listed above.
3. **Manual Entry:**
   * Alternatively, copy the path (e.g., `tests/test_csv_1.csv`) into the Path entry box and click **"Import"**.
4. **Validation:**
   * Check the terminal console for any caught exceptions.
   * Verify that the **Treeview** table reflects the data (or remains safe after a failed import).