from pseudo_random_generator import pseudoRandNumGen, numberOfDigits
import time as t
import random
import matplotlib.pyplot as plt
def generate(k):
    seed = int(str(t.time()).replace(".", "")) % 10**10
    # seed=8490255455
    x = pseudoRandNumGen(seed, k)
    # print(seed)
    # reverse the seed
    seed = reversed(str(seed))
    seed = int("".join(seed))
    y = pseudoRandNumGen(seed, k)
    # print(seed)
    return x, y

def inSquare(l):
    x, y = generate(l)
    max_len = max(numberOfDigits(x[0]), numberOfDigits(y[0]))
    # print(x,y)
    scale_factor = 10 ** max_len
    for i in range(len(x)):
        if x[i] % 2==0:
            # make it positive
            x[i]=x[i]/(10**10)
            x[i]=round(x[i],6) 
        else:
            x[i]=x[i]/(10**10)
            x[i]=1-x[i]
            x[i]=round(x[i],6)
    for i in range(len(y)):
        if y[i] % 2==0:
            y[i]=y[i]/(10**10)
            y[i]=round(y[i],6)
        else:
            y[i]=y[i]/(10**10)
            y[i]=1-y[i]
            y[i]=round(y[i],6)
    # print(x, y)
    return x, y

def estimate_pi(l):
    x, y = inSquare(l)
    count = sum(1 for i in range(len(x)) if x[i]**2 + y[i]**2 <= 1)
    return count / l * 4

def estimate_pi_using_random(l):
    x=[round(random.random()*2-1,6) for i in range(l) ]
    y=[round(random.random()*2-1,6) for i in range(l) ]
    # print(x,y)
    count=sum(1 for i in range(len(x)) if x[i]**2 + y[i]**2 <= 1)
    return count / l * 4    
def estimate_pi_error(l):
    return abs(l - 3.141592653589793)
if __name__ == "__main__":
    estPieError=[]
    randPieError=[]
    relError=[]
    bestPie=0
    for i in range(100):
        estPie=estimate_pi(1000)
        if(i==0):
            bestPie=estPie
        else:
            if (estimate_pi_error(estPie)<estimate_pi_error(bestPie)):
                bestPie=estPie
        randPie=estimate_pi_using_random(1000)
        plt.plot()
        estPieError.append(estimate_pi_error(estPie))
        randPieError.append(estimate_pi_error(randPie))
        relError.append(abs(estPie-randPie))
    print(f"CLosest value to π: {bestPie}")
    plt.plot(estPieError, 'r-', label='Estimate Pi Error', linewidth=2, alpha=0.7)
    plt.plot(randPieError, 'b-', label='Random Pi Error', linewidth=2, alpha=0.7)
    plt.plot(relError, 'g-', label='Relative Error', linewidth=2, alpha=0.7)
    plt.legend()
    plt.grid()
    plt.xlabel('Iteration')
    plt.ylabel('Error')
    plt.title('Error in estimation of π')
    plt.savefig('estimation_of_pie.png')
    plt.show()


# 668234434
# 434432866
# Replace the plot code with the following:
print(f"Closest value to π: {bestPie}")

# Enhance the graph's appearance
plt.figure(figsize=(10, 6))  # Set figure size for better visibility

# Plot errors with enhanced styles
plt.plot(estPieError, 'r-', label='Estimate π Error', linewidth=2.5, alpha=0.8, marker='o', markersize=5)
plt.plot(randPieError, 'b--', label='Random π Error', linewidth=2.5, alpha=0.8, marker='x', markersize=5)
plt.plot(relError, 'g-.', label='Relative Error', linewidth=2.5, alpha=0.8, marker='s', markersize=5)

# Add labels with larger font sizes
plt.xlabel('Iteration', fontsize=14, fontweight='bold')
plt.ylabel('Error', fontsize=14, fontweight='bold')
plt.title('Error in Estimation of π', fontsize=16, fontweight='bold', color='darkblue')

# Add a grid for better visual guidance
plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)

# Add legend with enhanced visibility
plt.legend(fontsize=12, loc='upper right', frameon=True, shadow=True, borderpad=1)

# Add annotations for better insight
plt.annotate(f"Closest to π: {bestPie:.5f}", 
             xy=(len(estPieError) - 1, estPieError[-1]), 
             xytext=(len(estPieError) - 20, max(estPieError) - 0.1),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=12, color='darkred')

# Save and show the graph
plt.savefig('estimation_of_pi_improved.png', dpi=300, bbox_inches='tight')  # High-quality save
plt.show()