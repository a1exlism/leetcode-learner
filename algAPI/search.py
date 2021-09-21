
visited = {}


def dfs(i):
    if (满足特定条件):
        # 返回结果 or 退出搜索空间
    visited[i] = True  # 将当前状态标为已搜索
    for 根据i能到达的下个状态j:
        if not visited[j]:  # 如果状态j没有被搜索过
            dfs(j)


visited = {}


def bfs():
    q = Queue()
    q.push(初始状态)
    while q.length:
        i = q.pop()
        if (visited[i]) continue
        for i的可抵达状态j:
            if j 合法:
                q.push(j)
    # 找到所有合法解
