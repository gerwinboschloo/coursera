def computepay(h,r):
    if h > 40.0:
        result = (h-40.0) * r*1.5 + (40.0) * r
    else:
        result= h*r
    return result

hrs = float(raw_input("Enter Hours: "))
rate = float(raw_input("What is the rate: ")) 

p = computepay(hrs,rate)
print p