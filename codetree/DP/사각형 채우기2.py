
'''
2 × n 크기의 사각형을 1 × 2, 2 × 1, 2 x 2 크기의 사각형들로 채우는 방법의 수를 구하는 프로그램을 작성해보세요
'''

# 0 0
# 1 1
# 2 3
# 3 5 3*1+1*2

# 4   5*1+3*2
# 5   11*1+5*2
n=int(input())
dp=[-1 for i in range(n+1)]

dp[0]=1
dp[1]=1

for i in range(2,n+1):
    dp[i]=(dp[i-1]+dp[i-2]*2)%10007

print(dp[n])
