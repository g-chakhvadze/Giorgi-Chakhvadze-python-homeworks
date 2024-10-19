# მომხმარებლისგან თარიღის მიღება
date_input = input("Input date: ")

# სტრიქონის განხილვა
date_part = date_input[:10]  # თარიღი
time_part = date_input[11:19]  # დრო
timezone_part = date_input[19:22]  # ზონის მართვის ნაწილი
timezone_sign = date_input[22:]  # "+" ან "-"

# თარიღის ნაწილების მიღება
year = date_part[:4]  # წელი
month = date_part[5:7]  # თვე
day = date_part[8:10]  # დღე

# დროის ფორმატირება
hour = int(time_part[:2])  # საათი
minute = time_part[3:5]  # წუთი
second = time_part[6:8]  # წამი

# საათის ფორმატირება
if hour > 12:
    hour -= 12

# გადაქცეული თარიღი
formatted_date = f"{day}-{month}-{year} {hour}:{minute}:{second} {timezone_sign}{timezone_part}"

# შედეგის დაბეჭდვა
print("Output:", formatted_date)
