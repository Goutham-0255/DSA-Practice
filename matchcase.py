import math

def switchCase(choice, arr):
        
        match choice:
            case 1:


                # AREA of circle formula (pi R^2)
                return math.pi*(arr[0]**2)
            case 2:

                # area of ractangle formula (L*B)
                return arr[0]*arr[1]
            case 3:
                
                return 'invalid number'
             
result1 = switchCase(1, [5]) 
result2 = switchCase(2, [5, 10])  
result3 = switchCase(3, [])


print(result1)