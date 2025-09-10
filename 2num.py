def twosum(arr, sum):
    res_list = []
    for i in range(0, len(arr)-1):
       one_num = arr[i]
       for j in range(i, len(arr)):
           if sum-one_num == arr[j]:
              res_list.append((one_num,arr[j])) 

    print(res_list)

arr = [7,1,2,8,3,4,7]
sum = 10
twosum(arr,sum)
               
            
        
