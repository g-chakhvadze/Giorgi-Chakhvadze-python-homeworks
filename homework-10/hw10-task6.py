from datetime import datetime
def car_info(manufacturer, year=datetime.now().year, **configurations):
    return {"Manufacturer": manufacturer, "Year": year, **configurations}

print(car_info("Toyota")) 
print(car_info("Ford", 2020)) 