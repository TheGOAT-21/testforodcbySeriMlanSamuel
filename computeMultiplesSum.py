def computeMultiplesSum(n):
    if 0 <= n < 1000:
        multiples_sum = 0
    
        for i in range(n):
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                multiples_sum += i
            
        return multiples_sum
    else :
        return "n doit etre compris entre 0 et 1000"

