def divisible_by_ten(num):
    if num % 10 ==0:
      return True
    else:
       return False
    
num = int (input("Enter a number: "))

answer = divisible_by_ten(num)
print ("your choice is :", answer)