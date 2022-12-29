import random
a = random.randint(-10,10)
b = random.randint(-10,10)

if a > 0 and b > 0:  
    print(f"x² +{a+b}x + {a*b}")
elif a*b <0: 
    print(f"x² -{a+b}x - {a*b}")
elif a < 0 and b < 0:
    print(f"x² -{a+b}x + {a*b}")