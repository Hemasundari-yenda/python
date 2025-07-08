import random
s=random.randint(1,100)

count=0
max_count=5
while count<max_count:
    num=int(input('guess the number!:'))
    count+=1
    if num>s:
        print('too high! Try again')
    elif num<s:
        print('too low!try again')
    
    
    else:
        print(f'you guess the correct number in {count} attempt')
else:
    print('No of attempts are done')