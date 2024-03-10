def large_power(base, exponent):
    if base^exponent > 5000:
        return True
    else:
        return False
    
base = int (input("Enter a number: "))
exponent = int (input("Enter power you wish to raise to: "))

answer= large_power (base, exponent)
print("The answer is:", answer)