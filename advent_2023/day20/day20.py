import queue
from copy import deepcopy
from collections import Counter

with open("day20_input.txt") as f:
    a = [i.replace("\n", "") for i in f.readlines()]

# load map
nodes = {}
for line in a:
    source, sinks = line.split(" -> ")
    sinks = sinks.split(", ")
    match source[0]:
        case "%":
            nodes[source[1:]] = {
                "name": source[1:],
                "source_type": "flipflop",
                "targets": sinks,
                "state": 0,
            }
        case "&":
            nodes[source[1:]] = {
                "name": source[1:],
                "source_type": "conjunct",
                "targets": sinks,
                "state": {},
            }
        case "b":
            nodes["broadcast"] = {
                "name": "broadcast",
                "source_type": "broadcast",
                "targets": sinks,
            }
        case _:
            ValueError("Missing type")

# Connect conjunction modules
conj_mods = [k for k, v in nodes.items() if v["source_type"] == "conjunct"]
for k, v in nodes.items():
    conj_in_targets = [i for i in conj_mods if i in v["targets"]]
    for conj in conj_in_targets:
        nodes[conj]["state"][k] = 0

stored_initial_state = deepcopy(nodes)
RX_PARENT = [k for k, v in nodes.items() if "rx" in v["targets"]][0]
TO_CHECK = {k: 0 for k, v in nodes.items() if any([i == RX_PARENT for i in v["targets"]])}


def push_the_button():
    q = queue.Queue()
    q.put((nodes["broadcast"], 0, "button"))
    # print("button -0-> broadcast")
    low_high = [1, 0]
    while not q.empty():
        node, signal_in, source_name = q.get()
        if node == "wait":
            continue

        if node["name"] == RX_PARENT:
            for k in TO_CHECK.keys():
                if node["state"][k] == 1 and TO_CHECK[k] == 0:
                    TO_CHECK[k] = PRESSES

        match node["source_type"]:
            case "broadcast":
                for sink in node["targets"]:
                    if sink not in nodes.keys():
                        continue
                    q.put((nodes[sink], signal_in, node["name"]))
                    # print(f"{node['name']} -{signal_in}-> {sink}")
                    low_high[signal_in] += 1
            case "flipflop":
                # update state
                if signal_in == 1:
                    continue

                node["state"] = 1 - node["state"]
                # push signal
                for sink in node["targets"]:
                    if sink not in nodes.keys():
                        q.put(("wait", "wait", "wait"))
                    else:
                        q.put((nodes[sink], node["state"], node["name"]))
                    # print(f"{node['name']} -{node['state']}-> {sink}")
                    low_high[node["state"]] += 1
            case "conjunct":
                # update state
                node["state"][source_name] = signal_in

                # push signal
                send_signal = not all(node["state"].values())

                for sink in node["targets"]:
                    if sink not in nodes.keys():
                        q.put(("wait", "wait", "wait"))
                    else:
                        q.put((nodes[sink], send_signal, node["name"]))
                    # print(f"{node['name']} -{send_signal}-> {sink}")
                    low_high[send_signal] += 1
    return low_high


# Part 1
counts = [0, 0]
for i in range(0, 1000):
    result = push_the_button()
    counts[0] += result[0]
    counts[1] += result[1]

print(f"Part 1: {counts[0] * counts[1]}")

# Part 2
# see cycle.png
nodes = stored_initial_state

PRESSES = 1
while not all(TO_CHECK.values()):
    push_the_button()
    PRESSES += 1

min_cycles = 1
for i in TO_CHECK.values():
    min_cycles *= i

print(f"Part 2: {min_cycles}")
