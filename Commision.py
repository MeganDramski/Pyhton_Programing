                        
def get_sales(sales):
     if sales < 10000:
          sales= sales *0.10        
     elif sales>=10000 and sales <=14999.99:
          sales = sales*0.12
     elif sales>=15000 and sales<=17999.99:
          sales =sales*0.14         
     elif sales >=18000 and sales <=21999.99:
          sales = sales*0.16         
     else:
           sales *0.18
     return sales
  
def determine_comm_rate(sales):
     if sales < 10000:
          rate = 0.10
     elif sales>=10000 and sales <=14999.99:
          rate = 0.12            
     elif sales>=15000 and sales<=17999.99:
          rate =0.14         
     elif sales >=18000 and sales <=21999.99:
          rate = 0.16          
     elif sales>22000:
          rate=0.18
     return rate

def advanced_pay(advanced):
    if advanced<=2000:
         return advanced
    else:return  print('An dcanaced pay cannot suceed 2000')
    
for i in range(3):
     names=input('Enter the name of the employee :')     
     monthly_sales = float(input('Enter the  monthly sales '))   
     advanced = float(input('Advanced pay:'))

     sales=get_sales(monthly_sales)
     adv_pay=advanced_pay(advanced)
     rate= determine_comm_rate(monthly_sales)

     pay= monthly_sales* rate -adv_pay
     print ('The pay  for ',names, 'is $ %.2f' %pay)

