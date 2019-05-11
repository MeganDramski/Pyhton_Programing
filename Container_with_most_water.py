array =[1,1]
l=len(array)
m=[]
for i in range(len(array)-1):
    pos=i+1    
    for j in range(len(array)-1,0,-1):
        end=j+1
        if len(array)<=2:
            vol=array[i]*i
            m.append(vol)
        if array[i]<=array[j]:
            distance=end-pos
            distance=abs(distance) 
            vol=array[i]*distance
            m.append(vol)
        
        elif array[i]>=array[j]:
            total=array[j]
            distance=end-pos
            distance=abs(distance)
            vol=total*distance
            
            m.append(vol)

       
print(max(m))
