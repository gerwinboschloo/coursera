from input import result
score = float(raw_input("Enter Score: "))
try:
    if score >= 0.9:
        result = "A"
    elif score >= 0.8:
        result  ="B"
    elif score >= 0.7:
        result = "C"
    elif score >= 0.6:
        result = "D"
    elif score < 0.6:
        result = "F"
    else:
        result = "Invalid number"  
    print result  
except:
     print("Invalid number" )
     
