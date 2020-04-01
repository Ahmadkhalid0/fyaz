#Каримзай Ахмад Халид
#ИУ7-15Б
#Practic programm

# List of prices for each area
prices = [
    { "step": 'A', "a": 0.10, "b": 0.06, "c": 0.02 },
    { "step": 'B', "a": 0.25, "b": 0.15, "c": 0.05 },
    { "step": 'C', "a": 0.53, "b": 0.33, "c": 0.13 },
    { "step": 'D', "a": 0.87, "b": 0.47, "c": 0.17 },
    { "step": 'E', "a": 1.44, "b": 0.80, "c": 0.30 }
]

phone_number = None 
Area_code = None
sh,sm,eh,em = None, None, None, None
#a,b,c = None, None, None

def getprice(i, index, a, b, c):# function to set prices
    if i <= 480:
        c += 1
        return prices[index]["c"], a, b, c

    if i <= 1080:
        a += 1
        return prices[index]["a"], a, b, c
    
    if i <= 1320:
        b += 1
        return prices[index]["b"], a, b, c
    
    c += 1
    return prices[index]["c"], a, b, c



Area_code = input("Area code: ").upper() # str
while Area_code != '#':
    ac = Area_code
    phone_nuber = input("Phone number: ")
    sh,sm,eh,em = map(int,input("Enter the start time and end times: ").split())

    a = 0 # Sum of rates from 8 am - 6 pm
    b = 0 # Sum of rates from 6 pm - 10 pm
    c = 0 # sum of rates from 10 pm - 8 am

    index = 0

    for index in range(5): #To find index
        if prices[index]["step"] == ac:
            break

    
    E = eh * 60 + em # End time 
    S = sh * 60 + sm # Start time
    sum = 0
    if S < E:# if start time is lower than end
        for i in range(S+1, E + 1):
            tmp, a, b, c = getprice(i, index, a, b, c)
            sum += tmp
            #print(sum)
    elif S == E:# if start time is equal with end time
        for i in range(S+1, 1440 + 1):
            tmp, a, b, c = getprice(i, index, a, b, c)
            sum += tmp
        for i in range(1, E + 1):
            tmp, a, b, c = getprice(i, index, a, b, c)
            sum += tmp
    else:# else
        for i in range(S + 1, 1441):
            tmp, a, b, c = getprice(i, index, a, b, c)
            sum += tmp
        for i in range(1, E + 1):
            tmp, a, b, c = getprice(i, index, a, b, c)
            sum += tmp
    #print("Phone Number\tCosts form 8 Am upto 6 Pm\
            #\t6 Pm upto 10 Pm\t10 Pm upto 8 Am\tTotally")
    print("\n{:10s} {:6d} {:6d} {:6d}   {:3s} {:8.2f}".format(phone_nuber, a, b, c, ac, sum))
    break
