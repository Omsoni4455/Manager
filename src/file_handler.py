import os

PATH = os.path.join("data", "expenses.txt")

def init_file():
    os.makedirs("data", exist_ok=True)
    if not os.path.exists(PATH):
        open(PATH, "w").close()

def save_data(date, category, t_type, amount):
    init_file()
    with open(PATH, "a") as f:
        f.write(f"{date}|{category}|{t_type}|{amount}\n")

def read_data():
    init_file()
    data = []
    with open(PATH, "r") as f:
        for line in f:
            if line.strip():
                p = line.strip().split("|")
                data.append({"date": p[0], "category": p[1], "type": p[2], "amount": float(p[3])})
    return data