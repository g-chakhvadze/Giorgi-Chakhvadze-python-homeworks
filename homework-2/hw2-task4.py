sichqare = float(input("ჩაწერეთ მანქანის სიჩქარე "))
sichqaris_kategoria = ""
if sichqare>0:
    if sichqare < 30 and sichqare > 0:
      sichqaris_kategoria = "SLOW"
    elif sichqare >= 120:
      sichqaris_kategoria = "VERY FAST"
    elif sichqare >= 60 and sichqare < 120 :
      sichqaris_kategoria = "FAST"
    elif sichqare >= 30 and sichqare < 60:
      sichqaris_kategoria = "MODERATE"
    print("მანქანის სიჩქარის კატეგორიაა " + sichqaris_kategoria)
elif sichqare == 0:
 print("მანქანა უძრავია")
else:
   print("ასეთი სიჩქარე ავტომობილს არ გააჩნია")
