import csv

total_revenue = 0
total_items = 0

with open("data/sales.csv", newline="") as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        price = float(row["price"])
        quantity = int(row["quantity"])
        
        revenue = price * quantity
        
        total_revenue += revenue
        total_items += quantity

print("Total revenue:", total_revenue)
print("Total items sold:", total_items)

products = {}

with open("data/sales.csv", newline="") as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        product = row["product"]
        quantity = int(row["quantity"])
        
        if product not in products:
            products[product] = 0
        
        products[product] += quantity

best_product = max(products, key=products.get)

print("Best selling product:", best_product)
