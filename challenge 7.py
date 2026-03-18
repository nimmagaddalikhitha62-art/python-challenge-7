readings = list(map(int, input().split()))
categories = {"efficient": [], "moderate": [], "high": [], "invalid": []}
for e in readings:
    if e < 0:
        categories["invalid"].append(e)
    elif e <= 50:
        categories["efficient"].append(e)
    elif e <= 150:
        categories["moderate"].append(e)
    else:
        categories["high"].append(e)
valid = [i for i in readings if i >= 0]
total = sum(valid)
summary = (total, len(readings))
eff = len(categories["efficient"])
mod = len(categories["moderate"])
high = len(categories["high"])
if total > 600:
    result = "Energy Waste Detected"
elif high >= 4:
    result = "Overconsumption Detected"
elif eff == mod or abs(eff - mod) == 1:
    result = "Balanced Usage"
elif eff > mod and eff > high:
    result = "Efficient Campus"
else:
    result = "Moderate Usage"
print(categories)
print("Total:", summary[0])
print("Buildings:", summary[1])
print(result)