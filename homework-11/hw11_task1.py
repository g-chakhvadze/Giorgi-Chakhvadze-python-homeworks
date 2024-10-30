def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 +32
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32)* 5/9
def main():
    celsius_values = [0,20,37,100]
    for celsius in celsius_values:
        fahrenheit = round(celsius_to_fahrenheit(celsius),3)
        print(f"{celsius}C = {fahrenheit}F")
    
    fahrenheit_values = [20,30,40,50]
    for fahrenheit in fahrenheit_values:
        celsius = round(fahrenheit_to_celsius(fahrenheit),3)
        print(f"{fahrenheit}F = {celsius}C")
    
main()