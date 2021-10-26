# 回溯法  栈  深度优先搜索
maze = [   # 创建迷宫
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,0,1,0,0,0,1,0,1],
    [1,0,0,1,0,0,0,1,0,1],
    [1,0,0,0,0,1,1,0,0,1],
    [1,0,1,1,1,0,0,0,0,1],
    [1,0,0,0,1,0,0,0,0,1],
    [1,0,1,0,0,0,1,0,0,1],
    [1,0,1,1,1,0,1,1,0,1],
    [1,1,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1]
]

class Stack:
    def __init__(self):
        self.stack = []
    def push(self,element):
        self.stack.append(element)
    def pop(self):
        return self.stack.pop()
    def get_top(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None
    def is_empty(self):
        return len(self.stack) == 0

dirs = [    # 四个方向
    lambda x,y : (x + 1,y),
    lambda x,y : (x - 1,y),
    lambda x,y : (x,y - 1),
    lambda x,y : (x,y + 1)
]
def maze_path(x1,y1,x2,y2):
    # x1,y1 是起点
    # x2,y2 是终点
    stack = []   # 创建一个栈
    stack.append((x1,y1))  # 起点入栈
    while(len(stack) > 0):  # 栈中有元素
        curNode = stack[-1]  # 当前的节点
        if curNode[0] == x2 and curNode[1] == y2:   # 如果到终点
            for p in stack:
                print(p)  # 输出路径点
            return True
        for dir in dirs:
            nextNode = dir(curNode[0],curNode[1])
            # 如果下一个节点能走
            if maze[nextNode[0]][nextNode[1]] == 0:
                stack.append(nextNode)
                maze[nextNode[0]][nextNode[1]] = 2   # 标记一下表示走过
                break
        else:
            maze[nextNode[0]][nextNode[1]] = 2   # 标记一下表示走过
            stack.pop()
    else:
        print("没有出路")
        return False

maze_path(1,1,8,8)
