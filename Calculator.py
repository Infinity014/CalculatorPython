def add(a,b):
    print(a+b)

def sub(a,b):
    print(a - b)

def mul(a,b):
    print(a*b)

def pow(m,n):
    ans = m
    for i in range(1,n):
        ans = ans*m
    print(ans)

def div(a,b):
    print(a/b)



while True:
    choice = input("Enter the opreation: [1]add [2]substract [3]multiply [4]divide [5]power [e]exit :  ")
    
    if choice == 'e':
        exit("Exited")
    
    a = input("Enter the number A: ")
    b = input("Enter The number B: ")
    
    try:
        a = int(a)
        b = int(b)
    except Exception as e:
        print(e)
        continue
    
    if choice  == '1':
        add(a,b)
        
    elif choice == '2':
        sub(a,b)
        
    elif choice == '3':
        mul(a,b)
        
    elif choice == '4':
        div(a,b)
        
    elif choice == '5':
        pow(a,b)
        
