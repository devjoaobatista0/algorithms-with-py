def sum(t: dict) -> int:
    if t["tag"] == "Leaf":
        return t["x"]
    else:
        return sum(t["x0"]) + sum(t["x1"])
    
print(sum(gen(24)))