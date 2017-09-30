import sys
from numpy import rate

try:
    hrs = float(raw_input("Enter Hours: "))
    rate = float(raw_input("What is the rate: "))   
    

    if hrs > 40.0:
        result = (hrs-40.0) * rate*1.5 + (40.0) * rate
    else:
        result= hrs*rate
    
    print("Pay: " , str(result))
except:
    print("Try numeric value") 