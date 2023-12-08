from multiprocessing import Process, Manager
from math import lcm

with open("day08_input.txt") as f:
    a = f.readlines()
    a = [i.replace('\n','') for i in a]

DIRS = [1 if i=='R' else 0 for i in a[0]]*1000

MAP = {}
for idx, row in enumerate(a[2:]):
    source, target = row.split(" = ")
    L,R = target.replace(")","").replace("(","").split(", ")
    MAP[source] = (L,R)

#Part 1
start, finish = "AAA", "ZZZ"
pos = [start]
for idx,dir in enumerate(DIRS):
    next =  MAP[pos[-1]][dir]
    pos.append(next)

    if next == finish:
        break

print(len(pos)-1)

#part 2
pos = [i for i in MAP.keys() if i[2]=="A"]
def get_z_pos(pos, return_dict, num):
    has_z = []
    for idx, dir in enumerate(DIRS):
        pos = MAP[pos][dir]
        if pos[2]=="Z":
            has_z.append(idx)
        if len(has_z) == 2:
            return_dict[num] = has_z[1] - has_z[0]
            break
    

if __name__ == "__main__":
    manager = Manager()
    return_dict = manager.dict()
    procs = []
    for num, i in enumerate(pos):
        new_proc = Process(target=get_z_pos, args=(i,return_dict,num))
        procs.append(new_proc)
        new_proc.start()

    for proc in procs:
        proc.join()
    
    cycles = return_dict.values()
    print(lcm(*cycles))