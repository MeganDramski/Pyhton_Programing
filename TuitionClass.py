
count_one=count_three= count_four=count_two=0
fee_one=0
fee_two=0
fee_three=0
fee_four=0


for i in range (2):
   
    name = input ('What is your last name ')
    pinNumber = int(input('What is your four digit pin number '))
    print ('There are four choices for code:  under_grad_commuter   under_grad_resident   grad_commuter   grad_resident')
    code = input( 'Enter one of the four choices for code ')
    hours =  int(input (' Enter credit hours studied '))
    print('\n')


    if code == 'under_grad_commuter':
        fee = 550 * hours
        fee_one = fee_one + fee
        count_one+=1
            
    elif code == 'under_grad_resident':
        fee = 550 * hours
        fee_two= fee_two + fee
        count_two+=1
            
    elif code == 'grad_commuter':
        fee = 650 * hours
        fee_three= fee_three + fee
        count_three+=1
              
    elif code =='grad_resident':
        fee = 700 * hours
        fee_four= fee_four+ fee
        count_four+=1

    else:
        fee=0
        print('error in code')
        

 
total= fee_one+fee_two+fee_three+fee_four
total_people=count_one +count_two +count_three + count_four
print('\n')   
print('The total collected amount is: $', total)
print('Total people enrolled is :', total_people)
print('\n')
print('The total fee for under_graduate commuting is: $',fee_one)
print ('The total fee for undergraduate residents is: $',fee_two) 
print ('The total fee for graduate commuting is: $',fee_three)              
print ('The total fee for graduate residents is: $',fee_four)     
print('there are',count_one,'undergraduate commuters')
print('There are ',count_two,'undergraduate residents ')
print('Thre are',count_three, 'graduate commuters')
print('There are ',count_four,'gradate residents')

