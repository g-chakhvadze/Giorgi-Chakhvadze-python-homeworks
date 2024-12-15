def midpoint(x1, y1, x2, y2):
    mid_x = (x1 + x2) / 2
    mid_y = (y1 + y2) / 2
    return (mid_x, mid_y)

def main():
    print("result 1:", midpoint(1, 2, 3, 4))
    print("result 2:", midpoint(-1, -2, 1, 2))
    print("result 3:", midpoint(0, 0, 4, 6))
    print("result 4:", midpoint(-3, -5, 3, 5))
    print("result 5:", midpoint(2.5, 3.5, 4.5, 5.5))

main()
