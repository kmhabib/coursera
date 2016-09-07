largest = None
smallest = None

while True:
    num = raw_input("Enter a number: ")
    if num == "done" : break
    try:
       input = int(num)
    except:
       print "Invalid input"
       num = raw_input("Enter a number: ")
        
    if smallest is None:
        smallest = num
    if num > largest:
       largest = num    
    elif num < smallest:
       smallest = num
    #print num
print "Maximum is", largest
print "Minimum is", smallest
