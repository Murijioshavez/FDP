def load_file():
    filepath = "genesis.txt"
    file =  open(filepath, 'r', encoding='utf-8')
    lines = file.readlines()
    return lines

def set_environment(raw_file):
    env = []
    for line in raw_file:
        line = line.strip()
        env.append([int(c) for c in line])
    return env
my_file = load_file()
env = set_environment(my_file)

def print_env(env):
    for row in env:
        for cell in row:
            if cell == 1:
                print('■', end='')

            else:
                print(' ', end='')
        print()

def check_neighbors(env,x,y):
    L1 = [x-1, x, x+1]
    L2 = [y-1, y, y+1]
    for i in L1:
        for j in L2:
            if i == x and i == y:
                continue
            if env[i][j] == 1:
                count
print_env(env)