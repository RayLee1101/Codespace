class Cave_Class():
    def __init__(self, name, gold, path):
        self.name = name
        self.gold = gold
        self.path = path
        self.state = True

def dfs(current, all_cave, total = 0):
    stack = list(filter(lambda x: x.name == current and x.state, all_cave))
    if len(stack) == 0:
        return total
    stack = stack[0]
    stack.state = False
    total += stack.gold
    for i in stack.path:
        total = max(total, dfs( i, all_cave, total))
    return total

def main():
    total_cavs, first = input().split()
    all_cave = []
    for i in range(int(total_cavs)):
        data = input().split()
        all_cave.append(Cave_Class(data[0], int(data[1]), [data[2], data[3]]))
    print(dfs(first, all_cave))
main()