from src.file_handler import read_data

def show_summary():
    data = read_data()
    if not data:
        return print("\n[-] No data for analytics.")
    
    inc = sum(x['amount'] for x in data if x['type'] == 'Income')
    exp = sum(x['amount'] for x in data if x['type'] == 'Expense')
    expenses = [x for x in data if x['type'] == 'Expense']
    top = max(expenses, key=lambda x: x['amount']) if expenses else None

    print(f"\n--- FINANCIAL ANALYTICS ---")
    print(f"Total Income : ₹{inc}\nTotal Expense: ₹{exp}\nNet Balance  : ₹{inc - exp}")
    if top:
        print(f"Top Expense  : ₹{top['amount']} ({top['category']})")