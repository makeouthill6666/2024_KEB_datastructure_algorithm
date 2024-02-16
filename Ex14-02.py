def recursion_fibo(n) :
    global  count_recu
    count_recu = count_recu+1
    if n < 2 :
        return 1
    else :
        return recursion_fibo(n-1) + recursion_fibo(n-2)

def dynamicplan_fibo(n) :
    global count_dp
    memo = [1, 1]
    if n < 2 :
        return memo[n]
    else :
        for i in range(2, n+1) :
            memo.append(memo[i-1] + memo[i-2])
            count_dp = count_dp + 1
        return memo[n]


count_dp, count_recu = 0, 0

print('##30번째 피보나치 수열##')

res = recursion_fibo(30)
print(f'재귀함수 방식 --> 답: {res}, 반복수 : {count_recu}')

res = dynamicplan_fibo(30)
print(f'동적계획 방식 --> 답: {res}, 반복수 : {count_dp}')