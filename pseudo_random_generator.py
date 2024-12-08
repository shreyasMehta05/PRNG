import time as t
import matplotlib.pyplot as plt
def numberOfDigits(n):
    # assumption n is int
    return len(str(int(n)))

def pseudoRandNumGen(seed,k):
    seed = int(seed)
    num=numberOfDigits(seed)
    li=[]
    for i in range(k):
        
        num=numberOfDigits(seed)
        seed=seed**2
        if num%2==0:
            seed=seed%(10**int(3*num/2))
            seed=seed/(10**int(num/2))
            seed=int(seed)
        else:
            seed=seed%(10**int((3*num+1)/2))
            seed=seed/(10**int((num+1)/2))
            seed=int(seed)
        li.append(seed)
        # print(seed)
    return li

if(__name__=="__main__"):
    temp = t.time()
    k=input("Enter the number of random numbers to generate: ")
    temp=int(str(temp).replace(".",""))
    k=int(k)
    n=input("Enter the number of digits in the seed: ")
    n=int(n)
    l=pseudoRandNumGen(temp%10**n, k)
    for i in range(k):
        print(f"{i+1}. {l[i]}")
    for i in l:
        l[l.index(i)]=i/(10**n)
    plt.hist(l, bins=30, color='skyblue', edgecolor='black', alpha=0.7)
    plt.xlabel('Random Numbers')
    plt.ylabel('Frequency')
    plt.title('Frequency Distribution of Random Numbers')
    plt.grid(True)  # Add grid lines
    plt.show()