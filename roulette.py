
pocket_num=int(input ('enter the number: '))

for n in range(5):
               
    if pocket_num == 0:
       print('Green')
    elif pocket_num >=1 and pocket_num <= 10:
               if pocket_num %2== 0:
                    print('red')
               else:
                    print('black')
    elif pocket_num >=11 and pocket_num <=18:
               if pocket_num %2==0:
                    print('red')
               else:
                    print('black')
    elif pocket_num >=19 and pocket_num <= 28:
               if pocket_num%2==0:
                    print('black')
               else:
                    print('red')
    elif pocket_num >=19 and pocket_num <= 36:
                if pocket_num %2 == 0 :
                    print('red')
                else:
                    print('black')
    else:
        print('ERROR')
                            
                     
