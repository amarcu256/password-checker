# This function ensure, ensures an integer is provided by the user via a while loop
def ensure():
    placement = input("Please enter a number ")
    try:
        int(placement)
    except ValueError:
        ensure()
    return int(placement)

#Function average takes the average of all values entered into a list that are above the threshold parameter

def average(threshold):
    #Variable creation: Assortment is our list, total is the culmination of list values above threshold to be added, 
    # count is the number of times such items appear, and placement is the integer input by the user
    assortment = []
    total =0
    count=0
    value =0
    value = ensure()

    while (value>0 or value== 0):
        assortment.append(value)
        value = ensure()
    for i in assortment:
        if i>threshold:
            total+=i
            count+=1
        
    if count ==0:
        print("No valid values entered! Enter negative value only to end program")
        average(threshold)

print(average(5))

    
