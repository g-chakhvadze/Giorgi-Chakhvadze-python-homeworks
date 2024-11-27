def process_data_file():
    with open('data.txt', 'r') as data_file:
        lines = data_file.readlines()
    with open('small.txt', 'w') as small_file, open('high.txt', 'w') as high_file:
        for line in lines:
            user_name, product_name, amount, price = line.strip().split(',')
            amount = int(amount)
            price = float(price)
            total_cost = amount * price
            if total_cost < 10:
                small_file.write(line)
            else:
                high_file.write(line)

if __name__ == "__main__":
    process_data_file()
