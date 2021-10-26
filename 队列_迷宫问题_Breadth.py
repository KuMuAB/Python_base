from collections import deque

maze = [   # 创建迷宫
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,1,0,1],
    [1,0,0,1,0,0,0,1,0,1],
    [1,0,0,0,0,1,1,0,0,1],
    [1,0,1,1,1,0,0,0,0,1],
    [1,1,0,0,1,0,0,0,0,1],
    [1,0,1,0,0,0,1,0,0,1],
    [1,0,1,1,1,0,1,1,0,1],
    [1,1,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1]
]

dirs = [    # 四个方向
    lambda x,y : (x + 1,y),
    lambda x,y : (x - 1,y),
    lambda x,y : (x,y - 1),
    lambda x,y : (x,y + 1)
]

# 打印节点
def print_r(path):
    curNode = path[-1]
    realpath = []
    while curNode[2] != -1:
        realpath.append(curNode[0:2])
        curNode = path[curNode[2]]
    
    realpath.append(curNode[0:2])
    realpath.reverse()
    for node in realpath:
        print(node)

def maze_path_queue(x1,y1,x2,y2):
    queue = deque()
    queue.append((x1,y1,-1))
    path = []
    while len(queue) > 0:
        curNode = queue.popleft()
        path.append(curNode)
        if curNode[0] == x2 and curNode[1] == y2:   # 如果到终点
            for p in path:
                print_r(path)  # 输出路径点
            return True
        for dir in dirs:
            nextNode = dir(curNode[0],curNode[1])
            # 如果下一个节点能走
            if maze[nextNode[0]][nextNode[1]] == 0:
                queue.append((nextNode[0],nextNode[1],len(path) - 1))   # 后续节点进队，记录那个节点把他带进来的
                maze[nextNode[0]][nextNode[1]] = 2   # 标记一下表示走过
                break
    else:
        print("没有出路")
        return False

maze_path_queue(1,1,8,8)