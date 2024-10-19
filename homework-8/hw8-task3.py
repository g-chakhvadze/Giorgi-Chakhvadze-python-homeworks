date_input = input("Input date: ")

date_part = date_input[:10] 
time_part = date_input[11:19]  
timezone_part = date_input[19:22] 
timezone_sign = date_input[22:]  

year = date_part[:4]  
month = date_part[5:7] 
day = date_part[8:10]  

hour = int(time_part[:2]) 
minute = time_part[3:5]  
second = time_part[6:8]  

if hour > 12:
    hour -= 12

formatted_date = f"{day}-{month}-{year} {hour}:{minute}:{second} {timezone_sign}{timezone_part}"

print("Output:", formatted_date)