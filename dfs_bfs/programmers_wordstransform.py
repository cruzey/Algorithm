from collections import deque

def bfs(begin, target, words):
    # 단어목록에 타겟단어가 없을 시에 0 반환
    if not target in words:
        return 0

    queue = deque()
    queue.append((begin, 0))

    while queue:
        now, depth = queue.popleft()
        # 현재 단어가 타겟이면 깊이 반환
        if now == target:
            return depth

        for i in words:
            cnt = 0
            for j in range(len(i)):
                # 단어의 길이만큼 각 자리를 비교해서 같을 때마다 cnt 1증가
                if now[j] == i[j]:
                    cnt += 1
            # 비교한 단어가 하나의 알파벳만 빼고 동일할 때 queue에 포함되어 있지 않으면 깊이를 1 올려서 추가
            if cnt == len(i) - 1: 
                if not i in queue:
                    queue.append((i, depth + 1))


begin, target = map(str, input().split(", "))
words = list(map(str, input().split(", ")))

result = bfs(begin, target, words)

print(result)

