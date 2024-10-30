def gcd_iteration(a,b):
    while b!=0:
        a,b=b,a%b
    return a

def gcd_recursion(a,b):
    if b == 0:
        return a
    return gcd_recursion(b,a%b)

if __name__ == "__main__":
    a = int(input("enter a: "))
    b = int(input("enter b: "))
    gcd_it = gcd_iteration(a,b)
    gcd_rec = gcd_recursion(a,b)
    print(f"GCD of {a} and {b} (iterative way) is: {gcd_it}")
    print(f"GCD of {a} and {b} (recursive way) is: {gcd_rec}")