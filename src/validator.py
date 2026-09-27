def validate_amount(amt_str):
    try:
        val = float(amt_str)
        return (True, val) if val > 0 else (False, "Amount must be > 0")
    except ValueError:
        return (False, "Enter a valid number")

def validate_choice(choice, max_opt):
    return (True, int(choice)) if choice.isdigit() and 1 <= int(choice) <= max_opt else (False, None)