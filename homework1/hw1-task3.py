a=float(input("პირველი გვერდის სიგრძეა?"))
b=float(input("მეორე გვერდის სიგრძეა?"))
c=float(input("მესამე გვერდის სიგრძეა?"))
if a < b + c and b < a + c and c < a + b and a > 0 and b > 0 and c > 0:
   p = a + b + c
   print(f"პერიმეტრი არის {p}")
   s = (p / 2 * (p / 2 - a) * (p / 2  - b) * (p / 2 - c)) ** 0.5
   print(f"სამკუთხედის ფართობი არის {s}")
else:
   print("ასეთი გვერდების მქონე სამკუთხედი არ არსებობს.")