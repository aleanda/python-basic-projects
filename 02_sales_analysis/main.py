import csv

total_revenue = 0
total_items = 0
products = {}

with open("data/sales.csv", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        price = float(row["price"])
        quantity = int(row["quantity"])
        product = row["product"]

        revenue = price * quantity
        total_revenue += revenue
        total_items += quantity
        products[product] = products.get(product, 0) + quantity

top_product = max(products, key=products.get)

print(f"Total revenue: €{total_revenue:.2f}")
print(f"Total items sold: {total_items}")
print(f"Top product: {top_product}")
print("Sales by product:")
for product, quantity in products.items():
    print(f"- {product}: {quantity}")
