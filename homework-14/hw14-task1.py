
temperatures = [
    (33, 34, 28),  #monday
    (24, 31, 27),  # Tuesday
    (24, 23, 27),  # Wednesday
    (28, 32, 34),  # Thursday
    (33, 21, 28),  # Friday
    (20, 25, 31),  # Saturday
    (21, 31, 28)   # Sunday
]

daily_averages = []
total_average = 0

for i, temps in enumerate(temperatures):
    day_average = sum(temps) / len(temps)
    day_max = max(temps)
    day_min = min(temps)
    
    daily_averages.append(day_average)
    total_average += day_average
    
    print(f"Day {i+1}:")
    print(f"Average temperature: {day_average:.2f}")
    print(f"Maximum temperature: {day_max}")
    print(f"Minimum temperature: {day_min}")
    print("-----")

weekly_average = total_average / len(temperatures)
print(f"Weekly average temperature: {weekly_average:.2f}")
