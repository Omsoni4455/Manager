from src.tracker import add_entry, view_entries
from src.analytics import show_summary
from src.validator import validate_amount, validate_choice

def main():
    while True:
        print("\n==================================")
        print("  PERSONAL EXPENSE & INCOME TRACKER MANAGER")
        print("==================================")
        print("1. Add Income  2. Add Expense  3. View  4. Analytics  5. Exit")
        ok, ch = validate_choice(input("Choice: "), 5)
        if not ok:
            print("[!] Invalid choice!"); continue

        if ch in (1, 2):
            t_type = "Income" if ch == 1 else "Expense"
            cat = input("Category: ").strip() or "General"
            ok_a, amt = validate_amount(input("Amount: "))
            if ok_a: add_entry(t_type, cat, amt)
            else: print(f"[!] {amt}")
        elif ch == 3: view_entries()
        elif ch == 4: show_summary()
        elif ch == 5: break

if __name__ == "__main__":
    main()