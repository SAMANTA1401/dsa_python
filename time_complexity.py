def Func(n):
    for i in range(1,n): ##n times
        j=1
        print('a')
        while j<i*i:  ## nxn times
            print('b')
            j=j+1
            if j%i ==0:
                for k in range(0,j): ## nxn times
                    print("krish")

# Func(5)
## total time complexity n^5 worst case

##2. 
def func(n):
    count=0
    for j in range(int(n/2),n):
        print('a')
        while j*2/2<=2:
            print('b')
            k=1
            while k<=n:
                print('c')
                count=count+1
                k=k*2
            j=j+1
        print(count)

func(4)