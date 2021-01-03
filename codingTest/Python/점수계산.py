# 점수계산
# OX문제는 맞거나 틀리거나 두가지 경우의 수가 있다.
# 여러개의 OX문제로 이루어진 시험에서는 연속적으로 문제를 맞추는 경우에는 가산점을 부과한다.
# 기본적으로 한문제를 맞추면 1점이고 연속적으로 맞으면 1, 2, 3점으로 가산점을 받게 된다.
# 시험문제의 결과가 주어졌을 때, 이 결과의 점수를 출력하는 프로그램을 작성하시오.
# ⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈⨈

n = int(input())
array = list(map(int, input().split()))
target = 0
score = 0

for i in range(len(array)):
    if array[i] == 0:
        target = 0
        continue
    target += 1
    score += target

print(score)

# ⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇⨇
# 풀이: 생략(easy)

# 문제: 생략

# 해결: 생략

# 느낀점:
#   이번에는 머리속으로 너무쉽다는 것을 인지해서인지 아주 빠르고 간단하게 해결할 수 있었다.
#   꾸준하게 풀이 하지 않으면 이런문제도 처음에 아무것도 할 수없었던 그때로 돌아가겠지. 꾸준히 계속 문제 푸는 습관을 가져야겠다.
