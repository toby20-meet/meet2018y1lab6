import random

random_num = random.randint(1,100)
print(random_num)
count = input('fizz? buzz? or fizzbuzz?')

for i in range(100):
    if (count) % 3 == 0 and count % 5 == 0:
        print('fizzbuzz')  
    elif(count) % 5 == 0:
        print("buzz")
    elif (count) % 3 == 0:
        print('fizz')
    else:
        print('ya wrong')
    
