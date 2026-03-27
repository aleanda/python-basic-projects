import csv

total_revenue = 0
customer_spending = {}
category_revenue = {}

with open("orders.csv", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        customer = row["customer"]
        category = row["category"]
        amount = float(row["amount"])

        # totale globale
        total_revenue += amount

        # spesa per cliente
        if customer not in customer_spending:
            customer_spending[customer] = 0
        customer_spending[customer] += amount

        # revenue per categoria
        if category not in category_revenue:
            category_revenue[category] = 0
        category_revenue[category] += amount

# cliente migliore
best_customer = max(customer_spending, key=customer_spending.get)

# categoria migliore
best_category = max(category_revenue, key=category_revenue.get)

print("Total revenue:", total_revenue)
print("Best customer:", best_customer)
print("Best category:", best_category)
