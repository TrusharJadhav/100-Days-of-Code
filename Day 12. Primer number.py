def is_prime(num):
    prime=[]
    for number in range(2,num):
        if num%number==0:
            prime.append("No")
    if "No" in prime:
        return False
    else:
        return True
    
print(is_prime(17))