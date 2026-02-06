import csv

CSV_PATH = "inventory (2).csv"

def load_prices(csv_path):
    prices = []
    items = []

    with open(csv_path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            prices.append(float(row["Price"]))
            items.append({
                "SKU": row["SKU"],
                "Name": row["Name"],
                "Price": float(row["Price"])
            })

    return prices, items

def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return seen[complement], i
        seen[num] = i
    return None

def main():
    target = float(input("Enter target price: "))

    prices, items = load_prices(CSV_PATH)
    result = two_sum(prices, target)

    if result:
        i, j = result
        print("\n✅ Match Found!")
        print(f"Indices: [{i}, {j}]")
        print(f"{items[i]['Name']} (${items[i]['Price']})")
        print(f"{items[j]['Name']} (${items[j]['Price']})")
        print(f"Total: ${items[i]['Price'] + items[j]['Price']}")
    else:
        print("\n❌ No matching pair found.")

if __name__ == "__main__":
    main()
