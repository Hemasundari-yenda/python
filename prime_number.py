num=int(input('enter the value'))
if num <=1:
    print('number is not a prime number')
else:
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            print("the number is not a prime number")
            break
    else:
        print('this is a prime number')
       
        

   
    


