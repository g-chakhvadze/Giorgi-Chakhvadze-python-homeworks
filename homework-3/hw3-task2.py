import random
#არამთელ რიცხვებში ჩავთვალე ყველა რიცხვი -1-დან 1-მდე.
random_num = random.uniform(-1,1)
print(random_num)
import math
rounded_down_num = math.floor(random_num*100) / 100
print(rounded_down_num)