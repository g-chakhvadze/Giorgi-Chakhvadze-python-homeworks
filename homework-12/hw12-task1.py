temps = [22,25,19,23,25,26,23]
def average_temp():
    total_temp = 0
    for i in range(len(temps)):
        total_temp+=temps[i]
    average_temp = total_temp/len(temps)
    return average_temp
    

if __name__ =="__main__":
   print(average_temp())
