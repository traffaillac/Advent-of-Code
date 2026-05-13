import json, re

I = input()

# part 1
print(sum(map(int, re.findall(r"[-]?\d+", I))))

# part 2
def count(node):
	if isinstance(node, int):
		return node
	elif isinstance(node, str):
		return 0
	elif isinstance(node, list):
		return sum(map(count, node))
	elif isinstance(node, dict):
		return 0 if "red" in node.values() else sum(map(count, node.values()))
print(count(json.loads(I)))
