import json
from collections import defaultdict

def process_sales_data():
    with open('data.txt', 'r') as data_file:
        lines = data_file.readlines()
    max_quantity = 0
    max_quantity_users = []
    total_values = defaultdict(float)
    total_quantities = defaultdict(int)
    product_counts = defaultdict(int)
    total_transactions = 0
    for line in lines:
        user_name, product_name, amount, price = line.strip().split(',')
        amount = int(amount)
        price = float(price)
        total_cost = amount * price
        if amount > max_quantity:
            max_quantity = amount
            max_quantity_users = [user_name]
        elif amount == max_quantity:
            max_quantity_users.append(user_name)
        total_values[user_name] += total_cost
        total_quantities[user_name] += amount
        product_counts[product_name] += amount
        total_transactions += 1

    max_total_value = max(total_values.values())
    max_total_value_users = [user for user, value in total_values.items() if value == max_total_value]
    average_total_value = sum(total_values.values()) / total_transactions
    average_quantity = sum(total_quantities.values()) / total_transactions
    max_product_count = max(product_counts.values())
    max_sold_products = [product for product, count in product_counts.items() if count == max_product_count]

    stats = {
        "max_quantity_users": max_quantity_users,
        "max_total_value_users": max_total_value_users,
        "average_total_value": average_total_value,
        "average_quantity": average_quantity,
        "max_sold_products": max_sold_products
    }
    with open('stats.json', 'w') as stats_file:
        json.dump(stats, stats_file, indent=4)

if __name__ == "__main__":
    process_sales_data()
