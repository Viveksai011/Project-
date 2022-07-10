# Faulty Calculator 

m = int(input("Enter a number :"))
n = int(input("Enter a number :"))
op = input("Enter a operator : '+,-,%,*,/' : ")
print("The answer is : ")
if m == 45 and n == 5 and op =='+':
    print('74')
elif m == 5 and n == 72 and op =='*':
    print('55')
elif m == 24 and n == 2 and op =='/':
    print('18')
elif m == 48 and n == 38 and op =='-':
    print('30')
elif op =='+':
    print(m+n)
elif op =='-':
    print(m-n)
elif op =='/':
    print(m/n)
elif op =='%':
    print(m%n)
elif op =='*':
    print(m*n)
else:
    print ('Syntex Error')

# Faulty Calculator By Vivek Sai
