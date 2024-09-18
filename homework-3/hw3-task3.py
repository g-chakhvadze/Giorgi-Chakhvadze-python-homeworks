#წლებზე,თვეებზე და დღეებზე შეზღუდვა არ მაქვს და თუ საჭიროა if statement-ს მოვაბამ.
birth_year = int(input("birth year date is? "))
birth_month = int(input("birth month number is? "))
birth_day = int(input("birth day number is? "))
import datetime
birth_time = datetime.date(birth_year,birth_month,birth_day)
#strftime ფუნქცია დავგუგლე რომ მენახა როგორ შემეძლო რიცხვის კვირის დღედ გარდაქმნა.
day_of_week = birth_time.strftime("%A")
print(f"you were born on {day_of_week}.")