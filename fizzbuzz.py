for i in range(100):
    count = i + 1
    if (count) % 3 == 0 and count % 5 == 0:
        print('fizzbuzz')  
    elif(count) % 5 == 0:
        print("buzz")
    elif (count) % 3 == 0:
        print('fizz')
    else:
        print(count)
    
