import os
import csv
import json

DEFAULT_FILE = "companies.txt"
DELIMITER = "|"

class CompanyManager:
    def __init__(self):
        self.companies = []
        self.current_file = DEFAULT_FILE
        self.load_initial_data()

    def load_initial_data(self):
        if os.path.exists(self.current_file):
            try:
                self.import_file(self.current_file)
            except Exception as e:
                print(f"Error loading initial file: {e}")

    def save_changes(self):
        if self.current_file.endswith('.json'):
            self.export_json(self.current_file)
        elif self.current_file.endswith('.csv'):
            self.export_csv(self.current_file)
        else:
            self.export_txt(self.current_file)

    def add_company(self, nit, name, address, budget):
        if self.nit_exists(nit):
            raise ValueError(f"A company with NIT {nit} already exists.")
        if not nit or not name or not address:
            raise ValueError("All fields are required.")
        try:
            budget = float(budget)
        except ValueError:
            raise ValueError("Budget must be a valid number.")

        new_company = {"nit": nit, "name": name, "address": address, "budget": budget}
        self.companies.append(new_company)
        self.save_changes()

    def update_company(self, original_nit, new_nit, name, address, budget):
        if original_nit != new_nit and self.nit_exists(new_nit):
            raise ValueError(f"The new NIT {new_nit} is already in use.")
        idx = self._find_index(original_nit)
        if idx is None: raise ValueError("Company not found.")
        try:
            budget = float(budget)
        except ValueError:
            raise ValueError("Budget must be a valid number.")

        self.companies[idx] = {"nit": new_nit, "name": name, "address": address, "budget": budget}
        self.save_changes()

    def delete_company(self, nit):
        idx = self._find_index(nit)
        if idx is None: raise ValueError("Company not found.")
        del self.companies[idx]
        self.save_changes()

    def nit_exists(self, nit):
        return any(e['nit'] == nit for e in self.companies)

    def _find_index(self, nit):
        for i, comp in enumerate(self.companies):
            if comp['nit'] == nit: return i
        return None

    def import_file(self, path):
        if not os.path.exists(path): raise FileNotFoundError(f"File not found: {path}")
        ext = os.path.splitext(path)[1].lower()
        new_data = []
        try:
            if ext == '.json':
                with open(path, 'r', encoding='utf-8') as f: new_data = json.load(f)
            elif ext == '.csv':
                with open(path, 'r', encoding='utf-8', newline='') as f: new_data = list(csv.DictReader(f))
            else:
                with open(path, 'r', encoding='utf-8') as f:
                    for line in f:
                        parts = line.strip().split(DELIMITER)
                        if len(parts) >= 4:
                            new_data.append({"nit": parts[0], "name": parts[1], "address": parts[2], "budget": parts[3]})
            self.companies = []
            for comp in new_data:
                self.companies.append({
                    "nit": str(comp.get('nit', comp.get('nit', ''))), 
                    "name": str(comp.get('name', comp.get('nombre', ''))), 
                    "address": str(comp.get('address', comp.get('direccion', ''))), 
                    "budget": float(comp.get('budget', comp.get('presupuesto', 0)))
                })
            self.current_file = path
        except Exception as e: raise Exception(f"Error reading file: {e}")

    def export_txt(self, path):
        with open(path, "w", encoding="utf-8") as f:
            for comp in self.companies: f.write(f"{comp['nit']}{DELIMITER}{comp['name']}{DELIMITER}{comp['address']}{DELIMITER}{comp['budget']}\n")

    def export_csv(self, path):
        with open(path, "w", encoding="utf-8", newline='') as f:
            w = csv.DictWriter(f, fieldnames=['nit', 'name', 'address', 'budget'])
            w.writeheader()
            w.writerows(self.companies)

    def export_json(self, path):
        with open(path, "w", encoding="utf-8") as f: json.dump(self.companies, f, indent=4, ensure_ascii=False)