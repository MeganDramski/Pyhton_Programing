year=[]
def collect_rainfall():    
    for month in range(12):       
        month=float(input ('Enter the amount of rainfall from January to December: '))
        year.append(month)


def print_months():
    for (index,value) in enumerate(year):
        index+=1    
        print('In the',index,'month of the year we had',value,'of rainfall')

collect_rainfall()
print('\n')
print_months()

print('\n')
def total():
    print('The total rainfall for the year is ', sum(year))
total()

def average():
    print('The average rainfall is %.2f'% float(sum(year))/len(year))
average()

def lowest():
    low = min(year)
    for month in year:
        if month==low:
            index=year.index(low)
            index=1+index
            print ('The month with the lowest amount is the ',index,'with the amount of rainfall of', month)             
lowest()

def highest():
    high = max(year)
    for month in year:
        if month==high:
            index=year.index(high)
            index=1+index   
            print ('The month with the hihest amount is the ',index,'with the amount of rainfall of', month)             
highest()
