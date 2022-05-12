n_terms = 8; 
  
# First two terms  
n_1 = 0  
n_2 = 1  
count = 0  
  
print ("The fibonacci sequence of the numbers is:")  
while count < n_terms:  
        print(n_1)  
        nth = n_1 + n_2  
       # At last, we will update values  
        n_1 = n_2  
        n_2 = nth  
        count += 1  