N = int(input("enter the number:"))
sum_even = 0


for i in range(0, N+1):
    if i%2 == 0 :
         sum_even +=1

print ("Sum of even numbers:",sum_even)
