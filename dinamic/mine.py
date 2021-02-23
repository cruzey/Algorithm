# n * m 크기의 금광을 testcase만큼 입력으로 받아 첫번째 열부터 출발하여 가장 많은 금을 캘수 있는 경우 구하기
# 금은 왼쪽 위, 왼쪽, 왼쪽 아래 3가지 경우에서 가져올 수 있다

testcase = int(input())
# 테스트케이스 만큼
for i in range(testcase):
    # 행렬 입력
    n, m = map(int, input().split(" "))
    # 금의 수 입력
    array = list(map(int, input().split(" ")))
    dp = []
    # 2차원 배열로 만들기 위한 인덱스
    index = 0
    # 열의 수만큼 슬라이싱
    for i in range(n):
        dp.append(array[index : index + m])
        index += m
    for j in range(1, m):
        for i in range(n):
            # 왼쪽 위 범위를 벗어나지 않도록
            if i == 0: left_up = 0
            else: left_up = dp[i - 1][j - 1]
            # 왼쪽 아래 범위를 벗어나지 않도록
            if i == n - 1: left_down = 0
            else: left_down = dp[i + 1][j - 1]
            left = dp[i][j - 1]
            # 세가지 경우 중 max
            dp[i][j] = dp[i][j] + max(left_up, left, left_down)
    result = 0
    # 마지막 열에서 가장 큰 수 출력
    for i in range(n):
        result = max(result, dp[i][m - 1])
    print(result)


