def authenticate():
   correct_pin=1234
   attempts=3

   while attempts>0:
      pin=int(input('enter the  4 digits pin:'))
      if pin==correct_pin:
         print('Access Granted!')
         return True
      else:
         attempts-=1
         print('enter the correct pin')

   print('acess denied')
   return False
Balance=50
def check_Balance():
   global Balance
   
   print(Balance)
def deposit_Balance(amount):
    global Balance
    Balance=Balance+amount
    print(Balance)
   
def withdraw_balance(amount):
   global Balance
   if amount<=Balance:
       Balance=Balance-amount
       print(Balance)
     
   else:
      print("Insufficient balance.")

if authenticate():
   while True:
      print('enter 1 for check balance')
      print('enter 2 for deposit money')
      print('enter 3 for withdraw money')
      print('enter 4 for exit')
      print('choose the options(1 to 4)')
      choice=int(input('enter your option'))
      if choice==1:
         check_Balance()
      elif choice==2:
         amount=int(input('enter the amount you want to deposit'))
         deposit_Balance(amount)
      elif choice==3:
         amount=int(input('enter the amount you want to withdraw'))
         withdraw_balance(amount)
      elif choice==4:
         print('Visit again')
      else:
         print('your choose incorrect input')
         break
      authenticate()