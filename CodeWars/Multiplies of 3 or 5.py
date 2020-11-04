def solution(number):
    retr_sum = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            retr_sum += i
    return retr_sum
  
print(solution(10))