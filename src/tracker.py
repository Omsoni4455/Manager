from datetime import datetime
from src.file_handler import save_data, read_data

def add_entry(t_type, category, amount):
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    save_data(now, category, t_type, amount)
    print(f"\n[+] {t_type} ₹{amount} added!")

def view_entries():
    data = read_data()
    if not data:
        return print("\n[-] No records found.")
    print("\nDate                 | Type    | Category   | Amount")
    print("-" * 55)
    for x in data:
        print(f"{x['date']} | {x['type']:<7} | {x['category']:<10} | ₹{x['amount']}")