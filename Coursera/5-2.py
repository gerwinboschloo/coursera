input_is_nok = False
smallest= None
highest = None
while True :

    num = raw_input("Enter a number: ")
    
    if num == "done" : 
        break
    
    try:
       val = int(num)
    except ValueError:
       print("Invalid input")
       continue
    n = int(num)
    if smallest is None:
        #first iteration
        smallest = n  
        highest = n 
    
    elif n > highest:
       highest = n
    elif n < smallest:
       smallest = n 

    
print('Maximum is', highest)
print('Minimum is', smallest)

