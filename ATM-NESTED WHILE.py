print('Welcom to SBI Bank')

chances=3
balance=15000.25

while chances >= 0:
    pin=int(input('Enter Your 4 Digit PIN:'))
    if pin==(2345):
        print('You Enetrerd Pin Correctly')
        restart = ('Y')
        while restart not in ('n','N','no','NO','No'):
            print('Please Press 1 To Check Balance:')
            print('Please Press 2 To Make a Withdraw:')
            print('Please Press 3 To Pay in:')
            print('Please Press 4 To Return Card:')
            option=int(input("What Would You Like To Choose? "))


            if option==1:
                print('Your balance is $',balance,'\n')
                restart=input('Would You Like To Go Back')
                if restart in ('n','N','no','NO','No'):
                    print('Thank you')
                    break
            elif option==2:
                option2=('Y')
                withdrawal=float(input("How Much Would You Like To Withdraw:\n$10,$20,$40,$60,$80,$100"))
                if withdrawal in (10,20,30,40,60,80,100):
                    balance=balance-withdrawal
                    print('Your balance is $', balance, '\n')
                    restart = input('Would You Like To Go Back')
                    if restart in ('n', 'N', 'no', 'NO', 'No'):
                        print('Thank you')
                        break
                elif withdrawal not in (10,20,30,40,60,80,100):
                    print('Invalid Amount,Please Retry')
                    restart=('y')

                elif withdrawal==1:
                    withdraw=float(input('Please Enter Desired Amount:'))


            elif option==3:
                pay_in=float(input('How Much Would You Like To Payin'))
                balance=balance+pay_in
                print('Your balance is $', balance, '\n')
                restart = input('Would You Like To Go Back')
                if restart in ('n', 'N', 'no', 'NO', 'No'):
                    print('Thank you')
                    break


            elif option==4:
                print('Please Wait Your Card is Returned......\n')
                print('Thank You For Your Service')
                break
            else:
                print('Please Enter a Correct Number')
                restart=('y')
    elif pin!=('2345'):
        print('Incorrect Password')
        chances=chances-1
        if chances==0:
            print('No More Tries')
            break






