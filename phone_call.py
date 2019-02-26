# the phone call problem

start_time = int ( input ( "What is the starting time of your phone call? "))
length =  input ( "What is the length of your phone call in minutes? ")
length= float(length)

regular_price = 0.40

if start_time >=1800:
    discounted_price = (regular_price *length)/2
    print ( 'The regular price for this call is: $ %0.2f' % (regular_price* length), '.The price after 50%% discounting starting time is $ %0.2f'% (discounted_price))
    if length>60:
        discounted_price=discounted_price-((discounted_price*15)/100)
        discount=(discounted_price*15)/100
        print('This call is eligible for extra 15%% discount which is: $ %0.2f'% (discount),'.The price with the additional discount is: %0.2f' %(discounted_price)) 
    elif length<60:
        discounted_price
elif start_time <=800:
    discounted_price= regular_price* length
    print('The price before tax for this call is: $ %0.2f' %(discounted_price))
    if length>60:
        discounted_price=discounted_price-((discounted_price*15)/100)
        discount=(discounted_price*15)/100
        print('This call is eligible for extra 15%% discount is which is: $ %0.2f'% (discount),'.The price with the additional discount is: %0.2f' %(discounted_price)) 
    elif length<60:
        discounted_price
else:
    discounted_price=regular_price+length
    
tax=(discounted_price*6.5)/100   
discounted_price= discounted_price+ tax



   
print ('The tax for this call is :$ %0.2f' %(tax))

print ( 'Your final price is %0.2f' %(discounted_price))
