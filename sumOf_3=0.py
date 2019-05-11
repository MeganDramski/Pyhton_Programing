nums = [-1, 0, 1, 2, -1, -4]
sol=[]
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        for k in range(j+1,len(nums)):
            row=[]
            if nums[i]+nums[j]+nums[k]==0:
                row.append([nums[i],nums[j],nums[k]])
                sol.append(row)
     
print(sol)
            
