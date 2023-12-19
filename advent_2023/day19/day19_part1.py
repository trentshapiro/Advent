import re

with open("day19_input.txt") as f:
    rules, inputs = f.read().split("\n\n")
    rules = rules.split("\n")
    inputs = inputs.split("\n")

rule_dict = {}
for rule in rules:
    name, rest = rule.split("{")
    checks = rest[:-1].split(",")
    name_list = []
    for check_num, check in enumerate(checks):
        if check_num == len(checks) - 1:
            name_list.append({"source": "any", "op": "any", "comp": "any", "target": check})
            continue
        name_list.append(
            {
                "source": re.findall("[a-z](?=\<|\>)", check)[0],
                "op": re.findall("\<|\>", check)[0],
                "comp": int(re.findall("(?<=\<|\>)[0-9]+(?=:)", check)[0]),
                "target": re.findall("(?<=:)[A-z]+", check)[0],
            }
        )

    rule_dict[name] = name_list


def follow_the_rules(element: dict[str], rule: str) -> int:
    if rule == "R":
        return 0
    if rule == "A":
        return 1

    rules = rule_dict[rule]
    compare = [i["source"] for i in rules if i["source"] in element.keys()]

    if not compare:
        return follow_the_rules(element, rules[-1]["target"])

    for rule in rules:
        comp_key = rule["source"]
        if comp_key == "any":
            return follow_the_rules(element, rule["target"])
        if comp_key not in element.keys():
            continue

        if (rule["op"] == "<" and element[comp_key] < rule["comp"]) or (
            rule["op"] == ">" and element[comp_key] > rule["comp"]
        ):
            return follow_the_rules(element, rule["target"])


# Part 1
total = 0
for line in inputs:
    elements = line[1:-1].split(",")
    elements = [i.split("=") for i in elements]
    elements = {k: int(v) for k, v in elements}
    accept = follow_the_rules(elements, "in")
    if accept > 0:
        total += sum(elements.values())
print(f"Part 1: {total}")
