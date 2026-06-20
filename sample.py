import random
from datetime import datetime

def generate_report():
    values = [random.randint(1, 100) for _ in range(10)]

    print("Sample Report")
    print("-" * 30)
    print(f"Generated: {datetime.now()}")

    print(f"Values: {values}")
    print(f"Highest: {max(values)}")
    print(f"Lowest : {min(values)}")
    print(f"Average: {sum(values) / len(values):.2f}")

if __name__ == "__main__":
    generate_report()