from manager import CompanyManager
import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def pause():
    input("\nPress ENTER to continue...")

def print_header():
    print("=" * 60)
    print("COMPANY MANAGEMENT SYSTEM (TERMINAL)")
    print("=" * 60)

def print_companies(companies):
    if not companies:
        print("\nNo companies registered.")
        return

    print("\n{:<15} {:<20} {:<25} {:>10}".format(
        "NIT", "NAME", "ADDRESS", "BUDGET"
    ))
    print("-" * 75)

    for c in companies:
        print("{:<15} {:<20} {:<25} {:>10.2f}".format(
            c["nit"], c["name"], c["address"], c["budget"]
        ))

def add_company(manager):
    clear()
    print_header()
    print("➕ ADD COMPANY\n")

    nit = input("NIT / ID: ").strip()
    name = input("Company name: ").strip()
    address = input("Address: ").strip()
    budget = input("Annual budget: ").strip()

    try:
        manager.add_company(nit, name, address, budget)
        print("\nCompany added successfully.")
    except Exception as e:
        print(f"\nError: {e}")

    pause()

def update_company(manager):
    clear()
    print_header()
    print("✏️ UPDATE COMPANY\n")

    nit_original = input("Enter existing NIT: ").strip()

    company = next((c for c in manager.companies if c["nit"] == nit_original), None)
    if not company:
        print("\nCompany not found.")
        pause()
        return

    print("\nLeave blank to keep current value.\n")

    new_nit = input(f"New NIT [{company['nit']}]: ").strip() or company["nit"]
    name = input(f"Name [{company['name']}]: ").strip() or company["name"]
    address = input(f"Address [{company['address']}]: ").strip() or company["address"]
    budget = input(f"Budget [{company['budget']}]: ").strip() or company["budget"]

    try:
        manager.update_company(nit_original, new_nit, name, address, budget)
        print("\nCompany updated successfully.")
    except Exception as e:
        print(f"\nError: {e}")

    pause()

def delete_company(manager):
    clear()
    print_header()
    print("🗑️ DELETE COMPANY\n")

    nit = input("Enter NIT to delete: ").strip()

    confirm = input(f"Are you sure you want to delete {nit}? (y/n): ").lower()
    if confirm != "y":
        print("\nCancelled.")
        pause()
        return

    try:
        manager.delete_company(nit)
        print("\nCompany deleted.")
    except Exception as e:
        print(f"\nError: {e}")

    pause()

def list_companies(manager):
    clear()
    print_header()
    print("COMPANY LIST")
    print_companies(manager.companies)
    pause()

def search_companies(manager):
    clear()
    print_header()
    print("SEARCH COMPANIES\n")

    term = input("Search by NIT or name: ").lower().strip()
    results = [
        c for c in manager.companies
        if term in c["nit"].lower() or term in c["name"].lower()
    ]

    print_companies(results)
    pause()

def export_data(manager):
    clear()
    print_header()
    print("EXPORT DATA\n")
    print("1. Export TXT")
    print("2. Export CSV")
    print("3. Export JSON")

    option = input("\nChoose format: ").strip()
    path = input("Enter output file path: ").strip()

    try:
        if option == "1":
            manager.export_txt(path)
        elif option == "2":
            manager.export_csv(path)
        elif option == "3":
            manager.export_json(path)
        else:
            print("\nInvalid option.")
            pause()
            return

        print("\nFile exported successfully.")
    except Exception as e:
        print(f"\nError: {e}")

    pause()

def main_menu():
    print("\n1. Add company")
    print("2. Update company")
    print("3. Delete company")
    print("4. List companies")
    print("5. Search companies")
    print("6. Export data")
    print("0. Exit")

def main():
    manager = CompanyManager()

    while True:
        clear()
        print_header()
        main_menu()

        choice = input("\nSelect an option: ").strip()

        if choice == "1":
            add_company(manager)
        elif choice == "2":
            update_company(manager)
        elif choice == "3":
            delete_company(manager)
        elif choice == "4":
            list_companies(manager)
        elif choice == "5":
            search_companies(manager)
        elif choice == "6":
            export_data(manager)
        elif choice == "0":
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid option.")
            pause()

if __name__ == "__main__":
    main()
