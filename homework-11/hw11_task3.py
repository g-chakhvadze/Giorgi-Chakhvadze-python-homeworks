from hw11_task2 import gcd_iteration
def lcm(a,b):
    return(a*b)//gcd_iteration(a,b)
def main():
    a = int(input("enter a: "))
    b = int(input("enter b: "))
    if 0 < a < 10000 and 0 < b < 10000:
        lcm_result = lcm(a,b)
        print(f"LCM of {a} and {b} is {lcm_result}")
    else:
        print("please enter natural numbers 0<a,b<10000.")
    
if __name__=="__main__":
    main()
